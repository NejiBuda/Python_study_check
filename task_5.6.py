"""
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

#my_fail = open('test_6.0.txt', 'w', encoding='utf-8')

import json

less = {}
numbers = "1234567890 "

with open("test_6.0.txt", "r", encoding="utf-8") as fail_obj:
    for line in fail_obj:
        subject, hours = line.split(":")
        less[subject] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(f"Total number of hours in the subject: \n {less}")





