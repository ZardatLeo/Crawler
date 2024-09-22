import re
import string
# 将文件转换为 UTF-8 编码
for i in range(1, 5): 
    file_path = './' + str(i * 2) + 'MB/' + str(i * 2) + 'MB_zh.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # 去除空白字符、制表符、换行符等
    data = [line.strip() for line in data if line.strip()]
    data_str = ''.join(data)  # 用换行符连接每一行
    data = data_str
    # 使用正则表达式移除中文标点符号
    data = re.sub(r'[，。！？、（）《》：“”；]', '', data)
    # 移除英文标点符号
    data = ''.join([char for char in data if char not in string.punctuation])
    # 删除数字
    data = re.sub(r'\d+', '', data)

    # 删除网址
    data = re.sub(r'http[s]?://\S+|www\.\S+', '', data)

    output_path = './' + str(i * 2) + 'MB/' + str(i * 2) + 'MB_zh_clean.txt'
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(data)