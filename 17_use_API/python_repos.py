from click import style
from colorama import Style
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储相应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print("Repositories return:", len(repo_dicts))

# # 研究第一个仓库17.1.5
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))

# for key in sorted(repo_dict.keys()):
#     print(key)

# 17.1.5
# print("\nSelect information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# 17.1.6
# print("\nSelect information about each repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

# 17.2.1
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = -45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15    # 将标签截断为15个字符，如果将鼠标指向被截断的标签，将显示完整标签
my_config.show_y_guides = False    # 隐藏图表中的水平线（y guide lines）
my_config.width = 1000

# show_legend=False 表示隐藏图例
# chart = pygal.Bar(style=my_style, x_label_rotation=-45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects On Github'
chart.x_labels = names

# 添加标签，鼠标悬停在柱状图上是第一行显示的文字
# chart.add('', stars)
chart.add('', plot_dicts)
chart.render_to_file('17_use_API\\python_repos.svg')