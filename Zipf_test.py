import re
from collections import Counter

with open('./8MB/8MB_en_clean.txt', 'r', encoding='utf-8') as file:
    data = file.read()

def rank(text):
    counter = Counter(text)
    lenth = len(counter)
    # 按值降序排序
    sorted_text = sorted(counter.items(), key=lambda item: item[1], reverse=True)

    # 将排序后的结果转换为字典
    sorted_text = dict(sorted_text)

    with open('Zipf_test.txt', 'w', encoding='utf-8') as file:
        file.write(str(sorted_text))

# 使用正则表达式匹配单词，忽略空格
words = re.findall(r'\S+', data)

rank(words)