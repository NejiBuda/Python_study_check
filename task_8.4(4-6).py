"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
"""

class Warehouse_of_office_equipment:

    def __init__(self, name, price, amount, list, *args):
        self.name = name
        self.price = price
        self.amount = amount
        self.num = list
        self.store_full = []
        self.store = []
        self.unit = {"Model" : self.name, "Price for one" : self.price, "Numbers" : self.amount}

    def __str__(self):
        return f"{self.name} price for one {self.price} numbers {self.amount}"

    @classmethod
    #@staticmethod
    def cash_register(self):
        print(f"To exit - End, Сontinuation - Enter")
        while True:
            try:
                unit_N = input(f"Enter name: ")
                unit_P = int(input(f"Enter price per piece: "))
                unit_A = int(input(f"Enter numbers: "))
                individ = {"Model" : unit_N , "Price for one" : unit_P, "Numbers" : unit_A}
                self.unit.update(individ)
                self.store.append(self.unit)
                print(f"Actual list: \n {self.store}")
            except:
                return f"Data entry error!"


            PF = input(f"/////")
            if PF == (End):
                self.store_full.append(self.store)
                print(f"Full stock: \n {self.store_full}")
                return f"Finish"
            else:
                return Warehouse_of_office_equipment.cash_register(self)




class Printer(Warehouse_of_office_equipment):
    def do_print(self):
        return f"to print something {self.num} times"

class Scanner(Warehouse_of_office_equipment):
    def do_scan(self):
        return f"to scan something {self.num} times"

class Xerox(Warehouse_of_office_equipment):
    def do_copy(self):
        return f"to copier something {self.num} times"

unit_1 = Printer("EPSON", 3000, 6, 12)
unit_2 = Scanner("Canon", 2000, 5, 11)
unit_3 = Xerox("Xerox", 2500, 2, 8)

print(unit_1.cash_register())
print(unit_2.cash_register())
print(unit_3.cash_register())

print(unit_1.do_print())
print(unit_2.do_scan())
print(unit_3.do_copy())

