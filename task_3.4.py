# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
# оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование
# цикла.


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_int(y):
    try:
        int(y)
        return True
    except ValueError:
        return False


def is_negative(v):
    try:
        v = float(v)
        if v < 0:
            return True
        elif v > 0:
            return False
    except ValueError:
        return


def negative_degree(q, w):
    res = 1 / (q ** abs(w))
    print(f'{q} в {w} степени будет {res}')


a = input('Введите действительное положительное число: ')
while not is_number(a):
    a = input('Введено некорректное значение. Попробуйте еще раз: ')
while is_negative(a):
    a = input('Введено некорректное значение. Попробуйте еще раз: ')
a = int(float(a))

b = input('Введите целое отрицательное число: ')
while not is_int(b):
    b = input('Введено некорректное значение. Попробуйте еще раз: ')
while not is_negative(b):
    b = input('Введено некорректное значение. Попробуйте еще раз: ')
b = int(b)

negative_degree(a, b)
