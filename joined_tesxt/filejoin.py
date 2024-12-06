# Создаем словарь с файлами, сортированными по количеству строк
def lines_number(files):
    f_dic = {}
    for file in files:
        with open(file, 'rt') as f:
            lines = f.readlines() 
            f_dic[file] = len(lines)
    sorted_f_dic = dict(sorted(f_dic.items(), key=lambda item: item[1]))

    return sorted_f_dic
    
files = ['1.txt', '2.txt', '3.txt']
dic = lines_number(files)

# Объединяем в один файл
with open('joined.txt', 'w') as f:
    for file_name, line_count in dic.items():
        f.write(f'{file_name}\n')
        f.write(f'{line_count}\n')
        with open(file_name, 'r') as file:
            lines = file.readlines()
        f.writelines(lines)
        f.write('\n')
