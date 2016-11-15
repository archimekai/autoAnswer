# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/01/2016   10:24 PM

import utility
file = open('testJieba.txt', 'r')

import jieba

line = file.readline()
seperated = jieba.cut(line)
print(", ".join(seperated))

# 按段计算相似度
# def similarity(str1, str2)


from gensim import corpora, models, similarities
tfidf = models.TfidfModel(seperated)
print(tfidf[1])
