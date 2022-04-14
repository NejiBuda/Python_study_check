"""
Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк
"""

seconds = int(input('Enter time in seconds: '))
minutes = seconds//60
hours = minutes//60

print("%02s:%02d:%02d" % (hours, minutes % 60, seconds % 60))
