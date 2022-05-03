"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

#my_fail = open('test_5.0.txt', 'w', encoding='utf-8')

def nomenclature():
    try:
        with open("test_5.0.txt", "w+") as fail_obj:
            line = input("Please enter numbers separated by spaces: \n")
            fail_obj.writelines(line)
            my_num = line.split()
            print(sum(map(int, my_num)))
    except IOError:
        print("File error")
    except ValueError:
        print("Wrong number set. I/O error")
nomenclature()

