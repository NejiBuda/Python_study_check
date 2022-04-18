"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове.
"""

line = input("Enter the string: ")
word = []
number = 1
for elt in range(line.count(' ') + 1):
    word = line.split()
    if len(str(word)) <= 10:
        print(f" {number}) {word [elt]}")
        number += 1
    else:
        print(f"{number}) {word [elt] [0 : 10]}")
        number += 1

