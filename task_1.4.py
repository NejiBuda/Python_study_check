"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
"""

n = int(input('Enter five-digit numbers: '))
max = n%10
while n >= 1:
    n = n // 10
    if n% 10 > max:
        max = n % 10
    if n >= 9:
        continue
    else:
        print('Maximum digit in number', max)
        break
