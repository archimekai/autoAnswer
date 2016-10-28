# lexical analysis
from utility import *
import re
question = "为什么黄连特别苦"
ques_cut = [ "为什么_r", "黄连_n", "特别_d", "苦_a"]

key_words = find_key_words(ques_cut)

file = open('baiduBaike_Huanglian.txt')

# print(contains_key_words("《纲目》：黄连大苦大寒，用之降火燥湿，中病即当止，岂可久服，使肃杀之令常",
#                          key_words))

print(re.match("黄连", "黄连大苦大寒") is None)
print(re.match(u"苦", u"黄连大苦大寒") is None)
#
# for line in file:
#     if contains_key_words(line, key_words):
#         print(line)
