# -*-coding:utf8-*-
import re
import urllib.request


# 下载图片
def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'  # 正则表达式
    reg_img = re.compile(reg)  # 编译一下，运行更快
    html_code = html_code.decode('utf-8')  # python3
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        print(img)
        urllib.request.urlretrieve(img, './img/%s.jpg' % x)
        x += 1
        # print('----------正在下载第' + x + '图片---------')


# 读取网页内容
def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


print('-------网页图片抓取-------')
url = input('请输入url:')
if url:
    pass
else:
    print('---没有地址输入正在使用默认地址---')
url = 'http://tieba.baidu.com/p/2008746223'
# http://tieba.baidu.com/p/2008746223
print('----------正在获取网页---------')
html_code = get_html(url)
get_image(html_code)
print('-----------下载完成-----------')
