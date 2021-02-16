"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
"""


class Storage:
    storage_items = {}
    branch1 = {}

    @classmethod
    def tech_reception(cls, new_name, count):
        if new_name in cls.storage_items.keys():
            cls.storage_items[new_name] += count
        else:
            cls.storage_items[new_name] = count
        return cls.storage_items

    def move_tech(self, name, count):
        self.storage_items[name] -= count
        if name in self.branch1.keys():
            self.branch1[name] += count
        else:
            self.branch1[name] = count
        return self.storage_items, self.branch1


class OfficeEquip:
    def __init__(self, name, life_time, manufacturer):
        self.name = name
        self.life_time = life_time
        self.manufacturer = manufacturer

    def __str__(self):
        return f'Наименование: {self.name}, Производитель: {self.manufacturer}, срок службы: {self.life_time} г.'

    def __setattr__(self, key, value):
        if key == 'life_time':
            if 0 < value < 5:
                self.__dict__[key] = value
            else:
                print('Неверно введен срок службы')
        else:
            self.__dict__[key] = value


class Printer(OfficeEquip):
    def __init__(self, name, life_time, manufacturer, page_count):
        OfficeEquip.__init__(self, name, life_time, manufacturer)
        self.page_count = page_count


class Scanner(OfficeEquip):
    def __init__(self, name, life_time, manufacturer, points_count):
        OfficeEquip.__init__(self, name, life_time, manufacturer)
        self.points_count = points_count


class Copier(OfficeEquip):
    def __init__(self, name, life_time, manufacturer, copy_count):
        OfficeEquip.__init__(self, name, life_time, manufacturer)
        self.copy_count = copy_count


class BarcodeReader(OfficeEquip):
    def __init__(self, name, life_time, manufacturer, wire_length):
        OfficeEquip.__init__(self, name, life_time, manufacturer)
        self.wire_length = wire_length


printer = Printer('Принтер', 4, 'Xerox', 4500)
print(printer.name, printer.life_time)
printer.life_time = 12

copier = Copier('Копир', 4, 'Xerox', 3400)
print(copier.name, copier.life_time)
printer.life_time = 10

print(printer.__dict__)
print(printer)

Storage.tech_reception('Принтер', 30)
Storage.tech_reception('Принтер', 20)
Storage.tech_reception('Сканер', 34)
Storage.tech_reception('Ксерокс', 15)
print(Storage.storage_items)
st = Storage()
st.move_tech('Принтер', 12)
st.move_tech('Сканер', 10)
print(st.move_tech('Ксерокс', 5))



