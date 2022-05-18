"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumbers:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = "x + y * n"

    def __add__(self, other):
        print(f"Total z_1 and z_2 equals: ")
        return f"z = {self.x + other.x} + {self.y + other.y} * n"

    def __mul__(self, other):
        print(f"Product z_1 and z_2 equals: ")
        return f"z = {self.x + other.x} * {self.y + other.y} * n"

    def __str__(self):
        return f"z = {self.x} + {self.y} * n"

z_1 = ComplexNumbers(2, -2)
z_2 = ComplexNumbers(-5, -8)
print(f"Complex numbers is {z_1}")
print(f"Complex numbers is {z_2}")
print(z_1 + z_2)
print(z_1 * z_2)