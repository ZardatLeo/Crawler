import string
import re
from nltk.corpus import stopwords

with open("output_en.txt", "r", encoding="utf-8") as file:
    data = file.read()

# 去除空白字符、制表符、换行符等
data = [line.strip() for line in data if line.strip()]

# 移除英文标点符号
data = ''.join([char for char in data if char not in string.punctuation])
# 将所有英文字符转为小写
data = data.lower()

# 由于要验证齐夫定律，因此不进行停用词清理
# # 载入英文停用词
# stop_words = set(stopwords.words('english'))
# data = ' '.join([word for word in data.split() if word not in stop_words])

# 删除网址
data = re.sub(r'http\S+|www\S+', '', data)

# 去除重复行
data = list(set(data))

# 去除空行
data = [line for line in data if line.strip()]

with open("chean_en.txt", "w", encoding="utf-8") as file:
    file.write(data)