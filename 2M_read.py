# 每次增大2M读取英文文本
for i in range(1, 5):
    with open("output_en.txt", 'r', encoding='utf-8') as file:
        data = file.read(i * 2 * 1000 * 1000)
    file_name = './' + str(i * 2) + 'MB/' + str(i * 2) + 'MB_en.txt' 
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)

data = ''
# 每次增大2M读取中文文本
for i in range(1, 5):
    with open("output_zh.txt", 'rb') as file:
        data = file.read(i * 2 * 1000 * 1000)
    file_name = './' + str(i * 2) + 'MB/' + str(i * 2) + 'MB_zh.txt' 
    with open(file_name, 'wb') as file:
        file.write(data)