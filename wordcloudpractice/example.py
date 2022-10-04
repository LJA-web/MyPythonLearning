import wordcloud
import jieba
wc = wordcloud.WordCloud(width=1000,
						height=800,
						background_color = 'white')

file = open('D:\DESKTOP\python_work\词云图python示例\青少年沉迷手机.txt', encoding='UTF-8').read()
wc.generate(file)
wc.to_file('D:\DESKTOP\python_work\词云图python示例\青少年沉迷手机.png')
