"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
 При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Nulls:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = Nulls(10, 100)
print(Nulls.by_null(10, 0))
print(Nulls.by_null(10, 0.1))
print(div.by_null(100, 0))
