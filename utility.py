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



if __name__ == '__main__':
    doc_name = 'baiduBaike_huanglian.txt'
    url = r'http://baike.baidu.com/subview/21017/16128831.htm'
    file = open(doc_name, 'w', encoding='utf-8')
    file.write(download_clean_text_str(url))
    # print(download_clean_text_str(url))