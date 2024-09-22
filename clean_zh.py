import re
# 将文件转换为 UTF-8 编码
with open('output_zh.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# 去除空白字符、制表符、换行符等
data = [line.strip() for line in data if line.strip()]

# 使用正则表达式移除中文标点符号
data = re.sub(r'[，。！？、（）《》：“”；]', '', data)


with open('output_file.txt', 'w', encoding='utf-8') as file:
    file.write(data)