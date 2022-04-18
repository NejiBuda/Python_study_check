"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
"""

elements = int(input("Enter some number of list items: "))
my_list = []
a = 0
elt = 0
while a < elements:
    my_list.append(input("Enter the following list item: "))
    a += 1

for elts in range(int(len(my_list) / 2)):
    my_list[elt], my_list[elt + 1] = my_list[elt + 1], my_list[elt]
    elt += 2
print(my_list)

