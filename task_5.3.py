"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

#my_fail = open('test_3.0.txt', 'r', encoding='utf-8')

with open("test_3.0.txt", "r", encoding="utf-8") as my_fail:
    test_3 = []
    lower = []
    my_list = my_fail.read().split("\n")
    for n in my_list:
        n = n.split()
        if float(n[1]) < 20000:
            lower.append(n[0])
            test_3.append(n[1])
print(f"Less salary 20.000 {lower} avverage salary {sum(map(float, test_3)) / len(test_3)}\n")