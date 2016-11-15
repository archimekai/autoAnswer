# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/02/2016   11:29 PM

from utility import *
import jieba.posseg as pseg

question = "为什么哈密瓜特别甜"
ques_cut = list(pseg.cut(question))
for word, flag in ques_cut:
    print('%s %s' % (word, flag))

key_words = ['哈密瓜', '甜']

def contains_causality(s: str):
    relation_key_words = ['所以', '因此']
    for word in relation_key_words:
        if re.search(word, s) is not None:
            return True
    return False



print(key_words)

# a very simple boolean search
def contains_key_words(sentence: str, key_words):
    for word in key_words:
        if re.search(word, sentence) is None:
            return False
    return True

# 基线系统如何实现呢？
file = open('baiduBaike_hamigua.txt')
for line in file:
    if contains_key_words(line, key_words) and contains_causality(line):
        print(line)

