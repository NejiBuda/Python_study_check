"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""

my_fail = open('test_1.0.txt', 'w', encoding='utf-8')
line = input("Enter text to write to file:\n")
while line:
    my_fail.writelines(line)
    line = input("You can continue typing:\n")
    if not line:
        break

my_fail.close()
furniture = my_fail.readlines()
print(furniture)
my_fail.close()