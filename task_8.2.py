# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByNull:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def division(self):
        return DivisionByNull.divide_by_null(self.up, self.down)

    @staticmethod
    def divide_by_null(up, down):
        try:
            return up / down
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


div = DivisionByNull(10, 100)
print(div.division())
div_2 = DivisionByNull(10, 0)
print(div_2.division())
print(DivisionByNull.divide_by_null(100, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
