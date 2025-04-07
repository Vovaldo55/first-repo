#Створи функцію, яка приймає два числа і виводить їх суму.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Сума:", result)


#Завдання 2: Функція, яка приймає ім'я та вік, і виводить повідомлення про вік
def greet_with_age(name, age):
    print(f"Привіт, {name}! Тобі {age} років.")

greet_with_age("Іван", 30)


#Завдання 3: Функція, яка повертає найбільше з трьох чисел
def max_of_three(a, b, c):
    return max(a, b, c)

largest = max_of_three(5, 8, 2)
print("Найбільше число:", largest)

#Завдання 4: Функція з змінною кількістю аргументів
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print("Сума чисел:", result)


def describe_person(name, age, city="Невідоме місто"):
    # Перевіряємо на чоловічі і жіночі імена
    if name.endswith('а'):  # Це жіноче ім'я (на 'а' в кінці)
        name_case = name[:-1] + 'і'  # Заміна на "І"
    elif name.endswith('й'):
        name_case = name[:-1] + 'ю'
    elif name.endswith('я'):
        name_case = name[:-1] + 'Ї'
    else:
        name_case = name + "у"  # Додавання закінчення "У"

    # Формуємо рядок з відміненою формою імені
    print(f"{name_case} виповнилось {age} років і живе в місті: {city}.")

describe_person("Іван", 30, city="Київ")
describe_person("Анна", 25)  # Тут значення для city використаємо за замовчуванням
describe_person("Сергій", 30, city="Київ")
describe_person("Марія", 30, city="Київ")



def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Викликаємо функцію з іменованими аргументами
person_info(name="Іван", age=30, city="Київ", job="програміст")


# Чи можна комбінувати *args і **kwargs?
def combined_example(arg1, *args, **kwargs):
    print(f"Перший аргумент: {arg1}")
    print("Інші аргументи:")
    for arg in args:
        print(arg)
    print("Іменовані аргументи:")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

combined_example(1, 2, 3, 4, name="Іван", age=30)


def describe_person(name, *args, **kwargs):
    print(f"Ім'я: {name}")

    print("Інші аргументи (позиційні):")
    for arg in args:
        print(arg)

    print("Іменовані аргументи (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person("Іван", 30, "Київ", job="Програміст", hobby="футбол")




