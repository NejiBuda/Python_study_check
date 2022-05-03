"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

#my_fail = open('test_2.0.txt', 'w', encoding='utf-8')
my_list = ['This \n', 'carpet\n','set\n', 'the\n', 'style\n', 'carpet\n', 'for\n', 'the\n', 'whole\n', 'room!\n']
with open("test_2.0.txt", 'w+') as file_ob:
    file_ob.writelines(my_list)
with open("test_2.0.txt") as file_ob:
    lines = 0
    notes = 0
    for line in file_ob:
        lines += line.count("\n")
        notes = len(line) - 1
        print(f"{notes} notes in line")
    print(f"Number of lines is {lines}")
