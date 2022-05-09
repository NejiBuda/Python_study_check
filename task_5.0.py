"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

#base class
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Start rendering {self.title}"

#child class
#№1
class Pen(Stationery):
    def __init__(self, titile):
        super().__init__(titile)

    def draw(self):
        return f"You are taking {self.title}. Start rendering pen."

#№2
class Pencil(Stationery):
    def __init__(self, titile):
        super().__init__(titile)

    def draw(self):
        return f"You are taking {self.title}. Start rendering pencil."

#№3
class Handle(Stationery):
    def __init__(self, titile):
        super().__init__(titile)

    def draw(self):
        return f"You are taking {self.title}. Start rendering handle."

#attribute values
pen = Pen("Ручка")
pencil = Pencil("Карнадаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())