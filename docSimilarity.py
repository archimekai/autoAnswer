# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/01/2016   11:20 PM

# 问题：为什么哈密瓜提别甜

text_truth = r'这与哈密瓜的产地有很大关系。哈密瓜产在我国的新疆吐鲁番盆地一带。那里夏天太阳刚刚升起，地面就热起来，到了中午地面把空气烤得很热，气温经常在四十摄氏度以上。一到晚上，气温又很快下降。由于那里早晚温差大，又很少下雨，很适于哈密瓜的生长。白天阳光强烈，哈密瓜的叶子就加紧制造养分，并把这些养分转化成糖分，送到瓜里存起来，晚上气温低，哈蜜瓜休息了，呼吸很慢，养分消耗就少了。所以哈密瓜长得又大又甜。'
text_test = r'哈密瓜性喜充足的阳光和较大的昼夜温差，白天可以充分发挥光合作用，而夜晚的呼吸消耗较小，有利于养分沉淀，因此糖分含量高，味极香甜。'
text_test_irrelevant = r'主要病害有白粉病，应降低荫蔽度增加光照并可用石硫合剂防治。虫害有蛴螬、蝼蛄等，可用毒饵诱杀。早春有麂子、锦鸡为害花苔和种子，应围以篱笆，加强人工捕杀，减较为害。'
# text_test = text_test_irrelevant

import jieba
from utility import *


# jieba.analyse.set_stop_words('chineseStopWords.txt')

tokens_truth = list(jieba.cut(text_truth))
tokens_test = list(jieba.cut(text_test))

# 需要去除停用词
file = open('chineseStopWords.txt', 'r', encoding='utf-8')
stopwords = []
for line in file:
    stopwords.append(line.strip())
tokens_test = remove_stop_words(tokens_test, stopwords)
tokens_truth = remove_stop_words(tokens_truth, stopwords)


from gensim import corpora, models, similarities
dictionary = corpora.Dictionary([tokens_test, tokens_truth])
print(dictionary)
vec_truth = dictionary.doc2bow(tokens_truth)
vec_test = dictionary.doc2bow(tokens_test)
print(cos_sparse_vector(vec_truth, vec_test))
# corpus_model = models.TfidfModel()
