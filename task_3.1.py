"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""

def my_fiksik (x,y):
    try:
        g = x / y
        return g
    except ZeroDivisionError:
        return "'y' is not be a zero"
    except ValueError:
        return "Enter only number"
print(my_fiksik(int(input("Enter x = ")), int(input("Enter y = "))))
