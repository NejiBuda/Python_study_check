"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчёте на одного сотрудника
"""

revenue=float(input("Enter the company's revenue: "))
cost=float(input("Enter the comapany's cost: "))

if revenue > cost:
    print(f"The company is profitable. Return on revenue amounted - {revenue/cost:.2f}")
    employees=int(input("Enter the number of co-workers: "))
    print(f"Profit per co-workers is - {revenue/employees:.2f}")
elif revenue == cost:
    print("The company is running at zero")
else:
    print("The company is operating at a loss")
