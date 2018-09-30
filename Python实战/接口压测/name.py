# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

"""

随机取名

"""

name_list = []


def get_name(url):
    request = urllib.request.Request(url)  # 创建对名字大全网站get请求
    result = urllib.request.urlopen(request)  # 发出请求
    soup = BeautifulSoup(result.read(), 'html.parser')  # 生成可分析对象
    if soup.find_all("a", class_="btn btn2"):
        for name in soup.find_all("a", class_="btn btn2")[:15]:  # 遍历所有的姓氏链接，此处只获取前15个姓氏
            url = 'http:' + name.attrs['href']  # 找到姓氏链接，再次返回此函数
            get_name(url)
    elif soup.find_all('a', class_='btn btn-link'):
        for name in soup.find_all('a', class_='btn btn-link')[:10]:  # 找到不同姓氏的名字，此处只获取每个姓氏的前10个
            name_list.append(name.text)
            # print(name.text)
    #print(len(name_list))
    return name_list


if __name__ == '__main__':
    url = "http://www.resgain.net/xsdq.html"
    for x in get_name(url):
        print(x)
    # print(get_name(url))
