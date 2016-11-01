# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# 十一月/01/2016   1:49 AM


from bs4 import BeautifulSoup
import requests

url = r'http://baike.baidu.com/subview/21017/16128831.htm'
html = requests.get(url)
html.encoding = 'utf-8'
print(html.encoding)
# print(html.text)
doc = BeautifulSoup(html.text, "lxml")
for script in doc(["script", "style"]):
    script.extract()
print(doc.get_text())