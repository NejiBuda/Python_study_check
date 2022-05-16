"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, сдекоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""

class The_Data:
    def __init__(self, time):
        self.time = str(time)

    @classmethod
    def extract(cls,time):
        my_time = []

        for n in time.split():
            if n != '-' : time.extend(n) #append

        return int(time[0]), int(time[1]), int(time[2])

    @staticmethod
    def right(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    if 2022 >= year >= 0:
                        return f"All right"
        else:
            return f"Somewhere time travel"


    def __str__(self):
        return f"The current date: {The_Data.extract(self.time)}"

Xronos = The_Data("16 - 05 - 2022")
print(Xronos)
print(The_Data.right(11, 11, 2022))
print(Xronos.right(11 , 13, 2012))
print(The_Data.extract("11 - 11 - 2011"))
print(Xronos.extract("11 - 11 - 2020"))
print(The_Data.right(1, 11, 2000))