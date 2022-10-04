import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温和最低气温
# filename = '16_download_data\\\temperature\sitka_weather_07-2014.csv'
# filename = '16_download_data\\temperature\\sitka_weather_2014.csv'
filename = '16_download_data\\temperature\\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 调用enumerate()来获取每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # 不要忘记转化为int类型！！！！
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date, "missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
# plt.title("Daily high temperatures, July 2014", fontsize=24)
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
