# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

firms = {}
av_profit = {"average_profit": 0}

count = 0
with open("text_7.txt", "r", encoding="utf-8") as text:
    for line in text:
        content = line.split()
        firms[f'{content[1]} {content[0]}'] = float(content[2]) - float(content[3])
        if (float(content[2]) - float(content[3])) > 0:
            count += 1
            av_profit["average_profit"] = av_profit["average_profit"] + float(content[2]) - float(content[3])

print(firms)
av_profit["average_profit"] = av_profit["average_profit"] / count
print(av_profit)
b = [firms, av_profit]

with open("text_task_5.7.json", "w", encoding="utf-8") as write_f:
    json.dump(b, write_f, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
