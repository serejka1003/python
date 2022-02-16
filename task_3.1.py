# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
# их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации
# деления на ноль.

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def func(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return
    return print(round(c, 5))


a = input('Введите, пожалуйста, делимое: ')
while not is_number(a):
    a = input('Введено некорректное значение. Попробуйте еще раз: ')
a = float(a)
b = input('Введите, пожалуйста, делитель: ')
while not is_number(b):
    b = input('Введено некорректное значение. Попробуйте еще раз: ')
b = float(b)

if b == 0:
    print('Ошибка! На ноль делить нельзя')

func(a, b)
