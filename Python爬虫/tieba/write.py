# coding:utf-8
import utils

'''
爬取百度贴吧帖子图片
'''

url = 'http://tieba.baidu.com/p/1753935195'

html = utils.get_html(url)
print(html)
# 以写的方式打开pageCode.txt
pageFile = open('pageCode.txt', 'wb+')
# 写入
pageFile.write(html)
# 开了记得关
pageFile.close()
