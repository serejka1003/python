# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
# сумму наибольших двух аргументов.


def max_sum(a, b, c):

    """Сложение двух максимальных чисел из трех

    Функция принимает на вход 3 значения.
    Осуществляет проверку число ли это. Если нет - выводит ошибку
    Далее создает из чисел список, сортирует.
    Складывет 2 максимальных значения из 3х и выводит результат

    """

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return print("Это не число.")
    list = [a, b, c]
    list.sort()
    sum = list[1] + list[2]
    print(f'Сумма максимальных значений {list[1]} и {list[2]} равна {sum}')


max_sum(input("Введите значение 1: "), input("Введите значение 2: "), input("Введите значение 3: "))
