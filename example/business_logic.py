import aspect

from aspect_logic import LogCar


@aspect.bind(LogCar)
class Car:
    def __init__(self, car_speed):
        self.__car_speed = car_speed

    def move(self, rotation):
        print(f'move {rotation} with {self.__car_speed:=}')
