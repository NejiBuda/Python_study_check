"""
Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень.
"""
def my_fiksik(x, y):
    num = 1
    for i in range(abs(y)):
        num *=x
    if y >= 0:
        return num
    else:
        return 1 / num

print(my_fiksik(float(input("First value: ")), int(input("Second value: "))))

