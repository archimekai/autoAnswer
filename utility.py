# relevant functions
import re

class Word:
    def __init__(self, word, type):
        self.word = word  # eg: "黄连"
        self.type = type # eg:'v'



class Synonym:
    def __init__(self, word):
        self.orginal_word = word

def find_key_words(question_cut):
    key_words_types = ['v', 'n', 'a']
    key_words = []
    for word in question_cut:
        for type in key_words_types:
            if word.endswith(type):
                key_words.append(Word(word[: -2], type))

    return key_words


# a very simple boolean search
def contains_key_words(sentence: str, key_words):
    for word in key_words:
        # print(word.word)

        if re.search(word.word, sentence) is None:
            return False
    return True

# clean text
hypertextP = re.compile(r'<[^>]+>')
def clean_hypertext(str):
    return hypertextP.sub("", str)


from bs4 import BeautifulSoup
import requests


def download_clean_text(url: str, out_file_name: str):
    html = requests.get(url)
    html.encoding = 'utf-8'
    doc = BeautifulSoup(html.text, "lxml")
    for script in doc(["script", "style"]):
        script.extract()
    file = open(out_file_name, 'w', encoding='utf-8')
    file.write(doc.get_text())
    file.close()

remove_lf = re.compile(r'\n+')
def download_clean_text_str(url: str):
    html = requests.get(url)
    html.encoding = 'utf-8'
    doc = BeautifulSoup(html.text, "lxml")
    for script in doc(["script", "style"]):
        script.extract()
    contents = doc.get_text()
    return remove_lf.sub("\n", contents)


def gensim_sparse_vector_to_array(sv):

    result = []
    for ind, val in sv:
        result.insert(ind, val)
    return result

import math
def cos_sparse_vector(sv1: list , sv2: list):
    len1 = 0
    len2 = 0
    ss_temp = 0
    for ind, val in sv1:
        ss_temp += val*val
    len1 = math.sqrt(ss_temp)
    ss_temp = 0
    for ind, val in sv2:
        ss_temp += val * val
    len2 = math.sqrt(ss_temp)
    # 通过类似于双路归并的算法求 v1 * v2
    p1 = 0
    p2 = 0
    sv1_by_sv2 = 0
    while p1 < len(sv1) and p2 < len(sv2):
        ele1 = sv1[p1]
        ele2 = sv2[p2]
        if ele1[0] == ele2[0]:
            sv1_by_sv2 += ele1[1] * ele2[1]
            p1 += 1
            p2 += 1
        elif ele1[0] < ele2[0]:
            p1 += 1
        else:
            p2 += 1
    return 1.0 * sv1_by_sv2 / (len1 * len2)

if __name__ == '__main__':
    vector1 = [(0, 1), (1, 0)]
    vector2 = [(0, 0), (1, 1)]
    print(cos_sparse_vector(vector1, vector2))


def remove_stop_words(tokens: list, stopwords: list) -> list:
    new_tokens = []
    for token in tokens:
        if token not in stopwords:
            new_tokens.append(token)
    return new_tokens

def get_stop_words()->list:
    file = open('chineseStopWords.txt', 'r', encoding='utf-8')
    stopwords = []
    for line in file:
        stopwords.append(line.strip())
    return stopwords


import similarities as sim
def check_similarity(doc: str, truth: str):
    '''
    逐段检查文档与truth的相似度，返回最高的段落相似度
    :return:
    '''
    paras = doc.split('\n')
    similarities = []
    for para in paras:
        if len(para) < 5: #  段落的长度必须大于5
            similarities.append(0)
        else:
            similarities.append(sim.similarity(para, truth))
    return max(similarities)


if __name__ == '__main__':
    text_truth = r'这与哈密瓜的产地有很大关系。哈密瓜产在我国的新疆吐鲁番盆地一带。那里夏天太阳刚刚升起，地面就热起来，到了中午地面把空气烤得很热，气温经常在四十摄氏度以上。一到晚上，气温又很快下降。由于那里早晚温差大，又很少下雨，很适于哈密瓜的生长。白天阳光强烈，哈密瓜的叶子就加紧制造养分，并把这些养分转化成糖分，送到瓜里存起来，晚上气温低，哈蜜瓜休息了，呼吸很慢，养分消耗就少了。所以哈密瓜长得又大又甜。'
    file = open('baiduBaike_hamigua.txt')
    str = file.read()
    print(check_similarity(str, text_truth))

    pass


if __name__ == '__2main__':
    doc_name = 'baiduBaike_huanglian.txt'
    url = r'http://baike.baidu.com/subview/21017/16128831.htm'
    file = open(doc_name, 'w', encoding='utf-8')
    file.write(download_clean_text_str(url))
    # print(download_clean_text_str(url))