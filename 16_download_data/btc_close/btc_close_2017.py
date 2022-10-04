#======================================= 从网站导入数据 =======================================#
# from __future__ import (absolute_import, division,
#                         print_function, unicode_literals)
# from urllib import response

# from flask import request

# try:
#     # Python 2.x 版本
#     from urllib2 import urlopen
# except ImportError:
#     # Python 3.x 版本
#     from urllib.request import urlopen
# import json

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# # 读取数据
# req = response.read()
# # 将数据写入文件
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)
# # 加载数据写入文件
# file_urllib = json.loads(req)
# print(file_urllib)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import json
# import pygal
# import math
# from itertools import groupby

# # 将数据加载到一个列表中
# filename = '16_download_data\\btc_close\\btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)

# # # 打印每一天的信息（后期不需要）
# # for btc_dict in btc_data:
# #     date = btc_dict['date']
# #     month = int(btc_dict['month'])
# #     week = int(btc_dict['week'])
# #     weekday = btc_dict['weekday']
# #     close = int(float(btc_dict['close']))
# #     print("{} is month {} week {}, {}, the close price is {}RMB".format(date,month,week,weekday,close))

# # 创建5个列表，分别存储日期和收盘价（公用）
# dates = []
# months = []
# weeks = []
# weekdays = []
# close = []
# # 每一天的信息
# for btc_dict in btc_data:
#     dates.append(btc_dict['date'])
#     months.append(int(btc_dict['month']))
#     weeks.append(int(btc_dict['week']))
#     weekdays.append(btc_dict['weekday'])
#     close.append(int(float(btc_dict['close'])))

#=================================== 根据已有数据绘制“每日收盘价”折线图 ====================================#
# # x_label_rotation 让横坐标标签顺时针旋转20°，
# # show_minor_x_labels 告诉图形不用显示所有x轴标签
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价（￥）'
# line_chart.x_labels = dates
# N = 20 # x轴坐标每隔20天显示一次
# line_chart.x_labels_major = dates[::N]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('16_download_data\\btc_close\\收盘价折线图（￥）.svg')

#==================================== 根据已有数据绘制“半对数变换”折线图 ====================================#
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价（￥）'
# line_chart.x_labels = dates
# N = 20 # x轴坐标每隔20天显示一次
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('16_download_data\\btc_close\\收盘价对数变换折线图（￥）.svg')

#==================================== 根据已有数据绘制“收盘价均值”折线图 ===================================#
# # 难理解！！！
# # 收盘价均值函数
# def draw_line(x_data, y_data, title, y_legend):
#     xy_map = []
#     """
#         1、zip(x_data, y_data)：
#             表示将传入的日期列表months和收盘价列表closes
#             分别按顺序各取一个元素打包成元组列表组合成一个新的迭代器——zip类
#             即[(1,6928), (1,7070) …… (11,65583)]。
#         2、sorted函数：
#             对元组列表进行排序，得到了按照月份从小到大
#             同一月份的收盘价从小到大排序的元组列表[(1, 5383), (1,5566) …… (1,6928), (1,7070) …… (11,65583)]
#             这里sorted函数先把第一位从小到大排好，再排第二位，以此类推。
#         2、groupby函数是一个分组聚合函数
#         4、lambda函数：
#             lambda 参数列表: 对参数需要进行的操作
#             key=lambda _: _[0]就表示取列表中索引为[0]的值，并将返回值赋给key（下划线表示临时变量，仅用一次之后销毁）
#             key这个表达式表示groupby分组的依据，意味着按照元组列表的第一个元素进行分类。
#             每循环一次，得到一组数据，x就是分类的key值。
#             最后循环十一次，x=1~11，y则是对应的元组列表，得到：
#                 x: 1 y: [(1,5383), (1,5566) …… (1,7835)]
#                 2 [(2,6793), (2,6811) …… (2,8206)]
#                 ……
#     """
#     for x, y in groupby(sorted(zip(x_data,y_data)), key=lambda _:_[0]):
#         y_list = [v for _, v in y]
#         xy_map.append([x, sum(y_list) / len(y_list)])
#     x_unique, y_mean = [*zip(*xy_map)]
#     line_chart = pygal.Line()
#     line_chart.title = title
#     line_chart.x_labels = x_unique
#     line_chart.add(y_legend, y_mean)
#     line_chart.render_to_file(title+'.svg')
#     return line_chart

# # 收盘价月日均值
# idx_month = dates.index('2017-12-01')
# line_chart_month = draw_line(months[:idx_month], close[:idx_month], '16_download_data\\btc_close\\收盘价月日均值（￥）', '月日均值')
# line_chart_month

# # 收盘价周日均值
# idx_week = dates.index('2017-12-11')
# line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '16_download_data\\btc_close\\收盘价周日均值（￥）', '周日均值')
# line_chart_month

# # 星期均值
# idx_week = dates.index('2017-12-11')
# wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
# line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值（￥）', '星期均值')
# line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
# line_chart_weekday.render_to_file('16_download_data\\btc_close\\收盘价星期均值（￥）.svg')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

with open('16_download_data\\btc_close\\收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>')
    for svg in [
        '收盘价折线图（￥）.svg', '收盘价对数变换折线图（￥）.svg', '收盘价月日均值（￥）.svg',
        '收盘价周日均值（￥）.svg', '收盘价星期均值（￥）.svg'
    ]:
        html_file.write(
            '   <object type="image/svg+xml" data="{0}"height=500 > </object >\n'.format(svg))
    html_file.write('</body></html>')
