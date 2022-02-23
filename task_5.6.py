# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный
# предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить
# и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lessons = {}

with open("text_6.txt", "r", encoding='utf-8') as text:
    for line in text:
        content = line.split()
        lessons[content[0][:-1]] = 0
        lenth = len(line)
        i = 0
        while i < lenth:
            s_int = ''
            a = line[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < lenth:
                    a = line[i]
                else:
                    break
            i += 1
            if s_int != '':
                lessons[content[0][:-1]] = (lessons[content[0][:-1]] + int(s_int))
print(lessons)
