question = "含羞草为什么会“含羞”"
# change to

# lexical analysis
question = "含羞草为什么会害羞"
ques_cut = ["含羞草_n", "为什么_r", "会_vm", "害羞_v"]

# key word extraction
key_words_noun = []
key_words_verb = []
for word in ques_cut:
    if word.endswith('_n'):
        key_words_noun.append(word[:-2])
    if word.endswith('_v'):
        key_words_verb.append(word[:-2])
print(key_words_noun)
print(key_words_verb)

# a very simple boolean search
def contains_key_words(sentence: str):
    for word in key_words_verb:
        if re.match(word, sentence) is None:
            return False
    for word in key_words_noun:
        if re.match(word, sentence) is None:
            return False
    return True

# clean text
import re
text = open('baiduBaike_MimosaPudicaLinn.txt', encoding='utf-8')
cnt = 0
for line in text:
    if contains_key_words(line):
        print(cnt)
        print(line)
        cnt += 1

text.close()