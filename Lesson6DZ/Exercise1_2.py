"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность
первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
"""
import time


class TrafficLight:
    _color = ''

    def __init__(self, new_color):
        self._color = new_color

    def running(self, sl_time):
        print(self._color)
        time.sleep(sl_time)


count = 0
traffic_colors = {'red': 3, 'g': 2, 'green': 5}

flag = False
while count < 2:
    i = 0
    for color, sleep_time in traffic_colors.items():
        signal_order = ('red', 'yellow', 'green')
        if color != signal_order[i]:
            print('Light error! Exit program')
            flag = True
            break
        else:
            tl = TrafficLight(color)
            tl.running(sleep_time)
            i += 1
    count += 1
    if flag:
        break

