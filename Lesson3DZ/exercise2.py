def input_info(category_name):
    digit = input(f"Введите {category_name}: ")
    return digit


def user_input(**kwards):
    print(kwards)


name = input_info('имя')
surname = input_info('фамилию')
birth_year = input_info('Год рождения')
city = input_info('Город проживания')
mail = input_info('Е-мейл')
phone = input_info('телефон')

user_info = user_input(Имя = name, Фамилия = surname, Год_рождения = birth_year, Город_проживания = city, Email = mail, телефон = phone)
