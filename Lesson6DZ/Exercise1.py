"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность
первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
"""
import time


class TrafficLight:
    _color = ''

    def running(self, tr_colors):
        signal_order = ('red', 'yellow', 'green')
        i = 0
        for color, sleep_time in tr_colors.items():
            if color == signal_order[i]:
                _color = color
                print(_color)
                i += 1
                time.sleep(sleep_time)
            else:
                print(f'Неверныйк порядок вывода сигналов. Работа программы завершена!')
                break


count = 0
while count < 3:
    traffic_colors = {'red': 3, 'yellow': 2, 'green': 5}
    tl = TrafficLight()
    tl.running(traffic_colors)
    count += 1
