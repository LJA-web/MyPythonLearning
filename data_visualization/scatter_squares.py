# 散点图
import matplotlib.pyplot as plt

x_values = list(range(1,1001))    # x从 1 到 1000
y_values = [x**2 for x in x_values]

"""
    s 数据点大小
    edgecolor 轮廓颜色
    c 数据点颜色
        - 十六进制 #bbffaa
        - rgb (0, 0, 0.8)，注意最大数值并非255
        - 颜色映射：将参数c设置为y值列表，并使用参数cmap告诉pyplot使用哪个颜色来映射
"""
# plt.scatter(x_values, y_values, c='#bfa', edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

# 以下两个语句二选一
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')