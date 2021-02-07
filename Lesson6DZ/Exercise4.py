"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        if self.is_police:
            cop_car = 'Да'
        else:
            cop_car = 'Нет'
        return f'Скорость: {self.speed}, Цвет: {self.color}, Название: {self.name}, Полицейский автомобиль: {cop_car}'

    def show_speed(self, new_speed):
        self.speed = new_speed
        return f'Скорость автомобиля {self.speed}'

    def go(self):
        print('Машина в движении')

    def stop(self):
        print('Машина остановилась')

    def turn(self, turn_side):
        print(f'Машина повернула {turn_side}')


class TownCar(Car):
    def show_speed(self, new_speed):
        self.speed = new_speed
        if 0 <= new_speed <= 60:
            return f'Скорость автомобиля {self.speed} км/ч'
        else:
            return f'Вы превышаете скорость на  {self.speed - 60} км/ч'


class SportCar(Car):
    is_police = False


class WorkCar(Car):
    def show_speed(self, new_speed):
        self.speed = new_speed
        if 0 <= new_speed <= 40:
            return f'Скорость автомобиля {self.speed} км/ч'
        else:
            return f'Вы превышаете скорость на  {self.speed - 40} км/ч'


class Police(Car):
    is_police = True


work_car = WorkCar(60, 'Blue', 'Optimus Prime', False)
print(work_car.name)
print(work_car.show_speed(40))
work_car.go()
work_car.stop()
work_car.turn('Налево')

police_car = Police(120, 'black', 'Ford Queen Victoria', True)
print(police_car)
print(police_car.show_speed(90))
police_car.go()
police_car.stop()
police_car.turn('Направо')

race_car = SportCar(240, 'blue', 'Honda', False)
print(race_car.is_police)
print(race_car.show_speed(90))
race_car.go()
race_car.stop()
race_car.turn('to the left')
