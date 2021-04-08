# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов:TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределитеметод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)должно выводиться сообщение о превышении скорости.


class Car:
    speed = None
    color = None
    name = None
    is_police = True

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')
        if self.speed > 40:
            return f'{self.name} превысила скорость'
        else:
            return f'Скорость {self.name} не привышает нормы'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')
        if self.speed > 60:
            return f'{self.name} Превысила скорость'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            return f'{self.name} из полицейского управления'
        else:
            return f'{self.name} не принадлежит полиции'


audi = SportCar(100, 'Красная', 'Audi', False)
kia = TownCar(30, 'Черная', 'KIA', False)
lada = WorkCar(70, 'Белая', 'Lada', False)
ford = PoliceCar(110, 'Синий',  'Ford', True)

print(f'{audi.name} из полиции? {audi.is_police}')
print(audi.show_speed())
print(kia.turn_right())
print(kia.show_speed())
print(lada.color, lada.name)
print(lada.turn_left())
print(lada.show_speed())
print(f'{lada.name} из полиции? {lada.is_police}')
print(ford.police())
print(ford.show_speed())