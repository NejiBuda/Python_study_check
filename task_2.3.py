"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""

annual_cycle_list = ['winter', 'spring', 'summer', 'autumn']
annual_cycle_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Enter mounth by number: "))
if month == 1 or month == 12 or month == 2:
    print(annual_cycle_list[0])
    print(annual_cycle_dict.get(1))
if month == 3 or month == 4 or month == 5:
    print(annual_cycle_list[1])
    print(annual_cycle_dict.get(2))
if month == 6 or  month == 7 or month == 8:
    print(annual_cycle_list[2])
    print(annual_cycle_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(annual_cycle_list[3])
    print(annual_cycle_dict.get(4))
else:
    print("Are you from planet Earth!?")

