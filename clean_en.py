import string
import re
from nltk.corpus import stopwords

for i in range(1, 5):
    file_path = './' + str(i * 2) + 'MB/' + str(i * 2) + 'MB_en.txt'
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # 去除制表符和换行符，但保留文本中的空格
    data = [line.rstrip('\n\r\t') for line in data if line.rstrip('\n\r\t')]

    # 移除英文标点符号
    data = ''.join([char for char in data if char not in string.punctuation])
    # 将所有英文字符转为小写
    data = data.lower()

    # 由于要验证齐夫定律，因此不进行停用词清理
    # # 载入英文停用词
    # stop_words = set(stopwords.words('english'))
    # data = ' '.join([word for word in data.split() if word not in stop_words])

    # 删除数字
    data = re.sub(r'\d+', '', data)

    # 删除网址
    data = re.sub(r'http[s]?://\S+|www\.\S+', '', data)

    output_path = './' + str(i * 2) + 'MB/' + str(i * 2) + 'MB_en_clean.txt'
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(data)