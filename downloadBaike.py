# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/02/2016   10:22 PM

from utility import *

filename='baiduBaike_hamigua.txt'
url = r'http://baike.baidu.com/subview/22513/13990014.htm'

file = open(filename, 'w', encoding='UTF-8')
webcontent = download_clean_text_str(url)
file.write(webcontent)

file.close()