"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.
"""

from sys import argv

if len(argv) > 1:
    name_worker, time_worker, tariff, bonus = argv
    name_worker = str(name_worker)
    time_worker = int(time_worker)
    tariff = int(tariff)
    bonus = int(bonus)
    result = (time_worker * tariff) + bonus
    print(f"Employsee salate: {result}")




