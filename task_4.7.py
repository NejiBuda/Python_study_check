"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from math import factorial

def fact_gen(n: int):
    for n in range(1, n + 1):
        yield factorial(el)

if __name__ == '__main__':
    fact = input("Enter the number of factorials: ")

    try:
        value = int(fact)
    except ValueError as b:
        print(b)
        exit(1)

    for elt in fact(value):
        print(el)








