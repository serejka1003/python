#Спортсмен занимается ежедневными пробежками.
#В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
#Требуется определить номер дня, на который результат спортсмена составит
#не менее b километров. Программа должна принимать значения
#параметров a и b и выводить одно натуральное число — номер дня.

#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

#запрашиваем сколько пробедал в первый день и какая цель
a = int(input("Сколько вы сегодня пробежали: "))
b = int(input("Введите цель: "))

#задаем значение сколько спортсмен пробежал за текущий день. Изначально =а
c = a

#задаем переменную дни = 1
day = 1

#пока текущая дистанция С меньше цели B будем считать дни в цикле
while c < b:
    c *= 1.1
    day += 1

print(f'Спортсмен достигнет цели на {day} день, пробежав {c:0.2f}')