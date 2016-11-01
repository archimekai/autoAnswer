# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# 十一月/01/2016   1:17 AM

from utility import *


def clean_text(filename):
    file = open(filename + '.txt', 'r')

    out = open(filename + '_Cleaned.txt', 'w')

    for line in file:
        out.write(clean_hypertext(line))

if __name__ == '__main__':
    clean_text('baiduBaike_Huanglian')