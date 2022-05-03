"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
#my_fail = open('test_7.0.txt', 'r', encoding='utf-8')
#my_fail = open('test_7.1.json', 'w', encoding='utf-8')
import json

gain = {}
gn = {}
gun = 0
av_profit = 0
i = 0
with open("test_7.0.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        name, firm, income, cost = line.split()
        gain[name] = int(income) - int(cost)
        if gain.setdefault(name) >= 0:
            gun = gun + gain.setdefault(name)
            i += 1
    if i != 0:
        av_profit = gun / i
        print(f"Average profit: {av_profit:.2f}")
    else:
        print(f"Profit average - absent. We work hard, hard workers =(")
    gn = {"Average profit: " : round(av_profit)}
    gain.update(gn)
    print(f"Profit per company: {gain}")

with open("test_7.1.json", "w") as notes_js:
    json.dump(gain, notes_js)
    js_str = json.dumps(gain)
    print(f"Created a json file with the following content: \n", f"{js_str}")




