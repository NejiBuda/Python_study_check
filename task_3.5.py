"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.

"""

def my_sum ():
    sum_result = 0
    examle = False
    while examle == False:
        num = input("Input numbers or End for qoit: ").split()
        result = 0
        for elt in range(len(num)):
            if num[elt] == 'd' or num[elt] == 'End':
                examle = True
                break
            else:
                result = result + int(num[elt])
        sum_result = sum_result + result
        print(f"Current sum is {sum_result}")
    print(f"Your final sum is {sum_result}")

my_sum()

