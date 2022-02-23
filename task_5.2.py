# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт
# строк и слов в каждой строке.

import string

with open("file_for_task_5.2.txt", "r", encoding="utf-8") as f:
    total_line = 0
    for line in f:
        print(f'В {total_line + 1} строке {len(line[:-1])} символов и '
              f'{sum([i.strip(string.punctuation).isalpha() for i in line.split()])} слов')
        total_line += 1
    print(f'Всего {total_line} строк')
