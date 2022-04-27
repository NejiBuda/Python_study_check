"""
Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
повторение элементов списка прекратится.
"""

from itertools import count, cycle

scr_start = int(input("First number: "))
scr_finish = scr_start * 2 + 10 + 1

#Var №1

for n in count(scr_start):
    if n < scr_finish:
        print(n)
    else:
        break
del n
print("Finish Var №1")

#Var №2

mom_list = [n for n in range(scr_finish)]
count = 0
for a in cycle(mom_list):
    if count < scr_finish + 10:
        print(a)
        count +=1
    else:
        break
print("Finish Var №2")

