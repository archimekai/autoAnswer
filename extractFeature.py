# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/15/2016   10:35 PM

# 因果关系识别


# 首先需要归纳因果关系的要素
# 判明原因部分和结果部分。
# 以段落为单位，抽取其中的因果关系，存储在XML中
# 1.this/cause/QW
# 2.是否含有感兴趣的关键词
# 3.语法上的依存关系
# 4.polarity 极性

import re
from utility import *

# 识别因为所以
# 句式  因为 ...   所以  ...
# 可以采取提取window的方法

def getCausality(paragraph: str):
    # 两段式因果结构  因为 ...  所以 ...
    window_size = [20, 20]  # 向前录入20个词，向后录入20个词
    reason_starts_with = ['因为']
    effect_starts_with = ['所以']
    # 只要构成一对就好了
    for word in reason_starts_with:

        reason_starts = re.finditer(word, paragraph)
        for reason in reason_starts:
            print(reason.start(), reason.end())
            endpos = reason.end()
            for effect_key_word in effect_starts_with:
                effect_starts = re.finditer(effect_key_word,paragraph[endpos:])
                for effect in effect_starts:



if __name__ == '__main__':
    para = "因为哈密瓜生长在北方，所以哈密瓜很甜。因为太阳很大，所以太阳很热。"
    getCausality(para)

