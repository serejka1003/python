# Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.Функция
# должна принимать параметры как именованные аргументы.Осуществить вывод данных о пользователе
# одной строкой.

contacts = []
found = 0


def add_contact():
    n = input('Введите имя: ')
    ln = input('Введите фамилию: ')
    y = input('Введите год рождения ')
    c = input('Введите город: ')
    e = input('Введите e-mail: ')
    t = input('Введите телефон: ')
    contacts.append({"name": n, "last_name": ln, "year": y, "city": c, "e_mail": e, "phone": t})
    print(f"Добавлен контакт: {n.capitalize()} {ln.capitalize()}, {y} года рождения, город - {c.capitalize()}, "
          f"e-mail {e}, телефон {t}")


choice = input('Какую операцию хотите выполнить? \n'
               '1 - Добавить контакт \n'
               '2 - Найти контакт \n'
               '3 - Выход \n')

while choice != '3':
    if choice == '1':
        add_contact()
        choice = input('Какую операцию хотите выполнить? \n'
                       '1 - Добавить контакт \n'
                       '2 - Найти контакт \n'
                       '3 - Выход\n')
    elif choice == '2':
        request = input('Введите параметр для поиска: ')
        for i in contacts:
            if request in i.values():
                print(f'Найден контакт: {i.get("name").capitalize()} {i.get("last_name").capitalize()}',
                      i.get("year"), i.get("city").capitalize(), i.get("e_mail"), i.get("phone"))
                found = 1
        if found == 0:
            print("Контакт не найден!")
        elif found == 1:
            found = 0
        choice = input('Какую операцию хотите выполнить? \n'
                       '1 - Добавить контакт \n'
                       '2 - Найти контакт \n'
                       '3 - Выход\n')
    else:
        choice = input('Введено некорректное значение. Какую операцию хотите выполнить? \n'
                       '1 - Добавить контакт \n'
                       '2 - Найти контакт \n'
                       '3 - Выход\n')
print('Выход')
