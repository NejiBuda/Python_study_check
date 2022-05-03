"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

#my_fail = open('test_4.0.txt', 'r', encoding='utf-8')

rus_edition = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четрые"}
new_fail = []
with open("test_4.0.txt", "r", encoding="utf-8") as fail_obj:
    for n in fail_obj:
        n = n.split(' ', 1)
        new_fail.append(rus_edition[n[0]] + '  ' + n[1])
    print(new_fail)

with open("test_4.2.txt", "w", encoding="utf-8") as fail_obj_2:
    fail_obj_2.writelines(new_fail)