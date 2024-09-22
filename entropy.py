import math
from collections import Counter

def caculate_entropy(text):
    counter = Counter(text)
    total_chars = sum(counter.values())
    probabilities = {char: count / total_chars for char, count in counter.items()}

    entropy = -sum(p * math.log2(p) for p in probabilities.values())

    return entropy

for i in range(2):
    if i == 0: 
        lang = 'en'
    else:
        lang = 'zh'
    for j in range(1, 5):
        file_name = './' + str(j * 2) + 'MB/' + str(j * 2) + "MB_" + lang + '_clean.txt'
        with open(file_name, "r", encoding='utf-8') as file:
            data = file.read()
        print(str(j * 2) + 'MB_' + lang, 'entropy: ', caculate_entropy(data))
