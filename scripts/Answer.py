# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Oct/24/2016   19:30
# import jieba
# 用于从语料中提取有关内容进行回答

corpus = open('baiduBaike_FicusCarica.txt', encoding='utf-8')

question = "为什么无花果的花看不见？"
ques_cut = ["为什么_r", "无花果_n", "的_u", "花_n", "看_v", "不_d", "见_v", "?_w"]

# 取出词性为名词的词，搜索百科的条目
key_nouns = []
for word in ques_cut:
    if word.endswith("_n"):
        key_nouns.append(word[:-2])
        # search word

# 在百科条目中进一步搜索相关的名词，
# 将有关的实义动词，以及否定词拓展之后进行搜索和匹配，提取出目标句子
# 但是很多时候结果涉及到对段落的理解，指代消解等等问题
target_sentences = []




import re

answer = ["无花果", "花"]
cntline = 0
for line in corpus:
    print(str(cntline), "\n", line)
    cntline += 1
    for word in key_nouns:
        if not re.match(word, line) is None:
            answer.append(line)

print(answer)


# print(jieba.lcut(question, cut_all=False))
# step1 extract key words from question
