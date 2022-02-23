# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

with open("test_file_for_task_5.5.txt", "w+", encoding="utf-8") as a:
    b = [str(random.randint(1, 20)) for i in range(random.randint(1, 20))]
    a.write(f'{" ".join(b)}')
    a.seek(0)
    content = a.read().split()
    print(f'В файл записано: {content}')
    result = [int(item) for item in content]
    print(f'Сумма чисел равна {sum(result)}')
