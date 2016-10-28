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
    key_words_types = ['v', 'n', 'd']
    key_words = []
    for word in question_cut:
        for type in key_words_types:
            if word.endswith(type):
                key_words.append(Word(word[: -2], type))

    return key_words


# a very simple boolean search
def contains_key_words(sentence: str, key_words):
    for word in key_words:
        print(word.word)

        if re.match(word.word, sentence) is None:
            return False
    return True


