"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisByNoool:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def DivByNull(x, y):
        try:
            return (x / y)
        except:
            return (f"Division by zero is not allowed!")

div = DivisByNoool(10, 100)
print(DivisByNoool.DivByNull(10, 0))
print(DivisByNoool.DivByNull(10, 1))
print(div.DivByNull(100, 0))