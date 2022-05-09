"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    #atibutes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    #methods
    def go(self):
        return f"{self.name} is started!"

    def stop(self):
        return f"{self.name} is stopped!"

    def turn_right(self):
        return f"{self.name} is turned right!"

    def turn_left(self):
        return f"{self.name} is turned left!"

    def show_speed(self):
        return f"Current speed {self.name} is {self.speed}."

#child classes
#№1
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Present speed of town car {self.name} is {self.speed}.")

        if self.speed > 60:
            return f"Speed of {self.name} is higher than allowed for the area!!!"
        else:
            return f"Speed of {self.name} is normal for this area."

#№2
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

#№3
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Present speed of work car {self.name} is {self.speed}.")
        if self.speed > 40:
            return f"Speed of {self.name} is higher than allowed for the area!!!"

#№4
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

        def police(self):
            if self.is_police:
                return f"{self.name} is Garbage car!"
            else:
                return f"{self.name}  it's one of us."


#attribute values
nissan = WorkCar(35, "Black", "Nissan", True)
bmw = PoliceCar(120, "White", "BMW", True)
lumba = SportCar(200, "Yellow", "Lamborghini", False)
kamaz = TownCar(30, "Brown", "Kamaz", False)

print(nissan.turn_left())
print(f"When {bmw.turn_right()}, then {kamaz.stop()}")
print(f"{lumba.go()} with speed exactly {lumba.show_speed()}")
print(f"{kamaz.name} is {kamaz.color}")
print(f"Is {bmw.name} a police car? {bmw.is_police}")
print(f"Is {lumba.name} a police car& {lumba.is_police}")
print(kamaz.show_speed())
print(nissan.show_speed())
print(nissan.is_police)



