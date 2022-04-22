"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
"""

""""
name = input("Enter your name: ")
surname = input("Enter your surname: ")
year_of_birth = input("Enter your year_of_birth: ")
city = input("Enter your city: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")
"""

def my_fiksik(name, surname, year_of_birth, city, email, phone):
    return ' '.join([name, surname, year_of_birth, city, email, phone])
    print(f"name, surname, year_of_birth, city, email, phone")

print(my_fiksik(name= 'Andrew', surname= 'Bychkov', year_of_birth='2000', city='SPb', email='bychkov_aa2000@mail.ru', phone='+7(950)004-11-23'))