# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(f'Доход составляет {self._income.get("wage") + self._income.get("bonus")}')


a = Position("Иван", "Петров", "менеджер", 50000, 10000)
b = Position("Степан", "Стулов", "руководитель", 100000, 20000)

print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()
print('')
print(b.name)
print(b.surname)
print(b.position)
print(b._income)
b.get_full_name()
b.get_total_income()
