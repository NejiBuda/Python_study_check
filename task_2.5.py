"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_line = [7, 5, 3, 3, 2]
print(f"Rating - {my_line}")
num = int(input("Enter the number (0000 - end): "))
while num != 0000:
    for elt in range(len(my_line)):
        if my_line[elt] == num:
            my_line.insert(elt + 1, num)
            break
        elif my_line[0] < num:
            my_line.insert(0, num)
        elif my_line[-1] > num:
            my_line.append(num)
        elif my_line[elt] > num and my_line[elt + 1] < num:
            my_line.insert(elt + 1, num)
    print(f"currnt list - {my_line}")
    num = int(input("Enter the number: "))

