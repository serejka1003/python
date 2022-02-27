# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

import random


class Car:
    def __init__(self, color, name):
        self.speed = random.randint(1, 120)
        self.color = color
        self.name = name
        self.is_police = random.randint(0, 1)

    def go(self):
        print(f'Автомобиль {self.color} {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.color} {self.name} остановился')

    def turn(self):
        print(f'Автомобиль {self.color} {self.name} повернул на{random.choice(["право", "лево"])}')

    def show_speed(self):
        print(f'Автомобиль {self.color} {self.name} движется со скоростью {self.speed}')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = 0

    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.color} {self.name} движется со скоростью {self.speed}. Превышение скорости!')
        else:
            print(f'Автомобиль {self.color} {self.name} движется со скоростью {self.speed}')


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = 0


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = 0

    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.color} {self.name} движется со скоростью {self.speed}. Превышение скорости!')
        else:
            print(f'Автомобиль {self.color} {self.name} движется со скоростью {self.speed}')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = 1


a = Car("Красная", "Ламборгини")
a.go()
a.stop()
a.turn()
a.show_speed()
print(a.speed)
print(a.is_police)

b = TownCar("Черная", "Лада")
c = SportCar("Желтый", "Порш")
d = WorkCar("Белая", "Ока")
e = PoliceCar("Радужный", "Форд")

b.turn()
b.show_speed()
print(b.is_police)
c.turn()
c.show_speed()
print(c.is_police)
d.turn()
d.show_speed()
print(d.is_police)
e.turn()
e.show_speed()
print(e.is_police)
