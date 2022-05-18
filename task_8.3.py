"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
элемента. Вносить его в список, только если введено число. Класс-исключение должен не
позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""

class My_Error(TypeError):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                value = int(input("Enter values, please: "))
                self.my_list.append(value)
                print(f"Present list - {self.my_list}\n")
            except:
                print(f"Dangerous value!")
                sec_chance = input(f"Try again:) ")

                if sec_chance == type(str) or sec_chance == type(bool):
                    print(try_except.my_input())

                elif sec_chance == type(int):
                    self.my_list.append(value)
                    print(f"Present list - {self.my_list}\n")
                    continue

                elif sec_chance == 9999:
                    break
                    print(f"Finish")

try_except = My_Error(1)
print(try_except.my_input())




