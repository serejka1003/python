# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП

class Store:
    def __init__(self, capacity):
        self.capacity = capacity
        self.my_store = []
        self.dep = {}

    def get(self, obj, departament=''):
        if len(self.my_store) >= self.capacity:
            print(f'Склад заполнен!')
        else:
            if departament != '':
                a = 0
                for k, v in self.dep.items():
                    if k == departament:
                        self.my_store.append([obj.model, obj.is_working, obj.is_color, obj.is_lan])
                        self.dep.pop(k)
                        a = 1
                        print(f'Оборудование перенесено из {k} на склад \n'
                              f'Сейчас на складе {self.my_store}')
                        break
                if a != 1:
                    print(f'Такого оборудования в {departament} нет. Проверьте ввод')
            else:
                self.my_store.append([obj.model, obj.is_working, obj.is_color, obj.is_lan])
                print(f'Оборудование {obj.model} принято на склад. Сейчас на складе {self.my_store}')

    def give(self, obj, departament):
        success = 0
        for i in self.my_store:
            if i[0] == obj.model:
                self.dep[departament] = [i[0], i[1], i[2], i[3]]
                self.my_store.remove(i)
                success = 1
                print(f'Оборудование {i[0]} передано в {departament}')
                break

        if success != 1:
            print(f'Такого оборудования нет на складе!')
            for k, v in self.dep.items():
                if v[0] == obj.model:
                    print(f'Оборудование находится в {k}')
                    break

    def status(self):
        print(f'Сейчас на складе {self.my_store}')
        print(f'Сейчас в подразделениях {self.dep}')


class OrgMachines:
    def __init__(self, model, is_working, is_color, is_lan):
        self.model = model
        self.is_working = is_working
        self.is_color = is_color
        self.is_lan = is_lan

    def work(self, count):
        pass


class Printer(OrgMachines):
    def __init__(self, model, is_working, is_color, is_lan):
        super().__init__(model, is_working, is_color, is_lan)

    def work(self, count):
        if self.is_working == 1:
            print(f'Принтер напечатал {count} страниц')
        else:
            print(f'Принтер не работает! Верните его на склад')


class Scaner(OrgMachines):
    def __init__(self, model, is_working, is_color, is_lan):
        super().__init__(model, is_working, is_color, is_lan)

    def work(self, count):
        if self.is_working == 1:
            print(f'Отсканировано {count} страниц')
        else:
            print(f'Сканер не работает! Верните его на склад')


class Xerox(OrgMachines):
    def __init__(self, model, is_working, is_color, is_lan):
        super().__init__(model, is_working, is_color, is_lan)

    def work(self, count):
        if self.is_working == 1:
            print(f'Сделано {count} ксерокопий')
        else:
            print(f'Ксерокс не работает! Верните его на склад')


store_1 = Store(3)
printer_1 = Printer('PR152', 1, 1, 0)
printer_2 = Printer('PR102', 1, 1, 0)
printer_1.work(15)
scaner_1 = Scaner('SC152', 0, 1, 0)
scaner_1.work(10)
xerox_1 = Xerox('XR152', 1, 0, 1)
xerox_1.work(5)

store_1.get(printer_1, "Бухгалтерия")
store_1.get(printer_1)
store_1.get(xerox_1)
store_1.get(scaner_1)
store_1.get(printer_2)

store_1.give(printer_1, "Бухгалтерия")
store_1.give(printer_1, "HR")
store_1.give(xerox_1, "IT")
store_1.give(xerox_1, "Хоз блок")

store_1.status()

store_1.get(printer_1, "Бухгалтерия")
