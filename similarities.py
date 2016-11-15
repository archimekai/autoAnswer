# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/02/2016   5:28 AM

import jieba
from utility import *
from gensim import corpora, models, similarities


def similarity(test: str, truth: str):
    tokens_truth = list(jieba.cut(truth))
    tokens_test = list(jieba.cut(test))
    stopwords = get_stop_words()
    tokens_test = remove_stop_words(tokens_test, stopwords)
    tokens_truth = remove_stop_words(tokens_truth, stopwords)
    dictionary = corpora.Dictionary([tokens_test, tokens_truth])
    vec_truth = dictionary.doc2bow(tokens_truth)
    vec_test = dictionary.doc2bow(tokens_test)
    return cos_sparse_vector(vec_truth, vec_test)