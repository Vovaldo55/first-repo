def multiply(a,b):return a*b
def divide(a,b): return a/b
class calc:pass


class Hero:
    def say_hello(self):
        print("Привіт! Я герой!")

h = Hero()
h.say_hello()  # Це викликає метод через об'єкт h

print("Hello!") # ПЕРЕВІРКА ДЛЯ Git

#СТВОРЕННЯ КЛАСУ
class Car:
    # Конструктор класу
    def __init__(self, brand, model, year, motor):
        self.brand = brand  # Атрибут об'єкта
        self.model = model  # Атрибут об'єкта
        self.year = year    # Атрибут об'єкта
        self.motor = motor  # Атрибут об'єкта

    # Метод класу
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} {self.motor}")


my_car = Car("Toyota", "Corolla", 2020, 1.6)
my_car.display_info()  # Виведе: 2020 Toyota Corolla


#Створи клас Person, що містить атрибути:
class Person:
    # Конструктор класу
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    # Метод класу
    def display_info(self):
        print(f"{self.name} {self.age} {self.job}")

    def is_adult(self):
        return self.age >= 18



person1 = Person("Кулєбяка", 22, "ML розробник-аматор")
person2 = Person("Аліна", 17, "Python Developer")
person3 = Person("Семен", 35, "Data Scientist")
person4 = Person("Марко", 15, "AI Інженер")
# Додамо їх у список
people = [person1, person2, person3, person4]

# Пройдемось по списку та виведемо інформацію
for person in people:
    status = "✅ повнолітній" if person.is_adult() else "❌ неповнолітній"
    print(f"{person.name} ({person.age} років): {status}")


#Оновлений клас Person:
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job}")

    def is_adult(self):
        return self.age >= 18

    def greet(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років і я працюю як {self.job}.")

    def change_job(self, new_job):
        old_job = self.job
        self.job = new_job
        print(f"{self.name} змінив(ла) роботу: з '{old_job}' на '{self.job}'.")


person1 = Person("Кулєбяка", 22, "ML розробник-аматор")
person2 = Person("Аліна", 17, "Python Developer")
person3 = Person("Семен", 35, "Data Scientist")
person4 = Person("Марко", 15, "AI Інженер")

# Викликаємо методи
person4.greet()
person4.change_job("AI Researcher")
person4.display_info()
print()



# ОНОВЛЕНИЙЮ метод birthday(), спадкування через Student(Person)
# і перевірку на кардинальну зміну професії
# Клас Person — базовий клас для людей
class Person:
    # Ініціалізація (конструктор): задаємо ім’я, вік і роботу
    def __init__(self, name, age, job):
        self.name = name          # Зберігаємо ім'я у властивість name
        self.age = age            # Зберігаємо вік у властивість age
        self.job = job            # Зберігаємо роботу у властивість job

    # Метод, який виводить всю інформацію про людину
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job}")

    # Метод, що повертає True, якщо людина повнолітня (18+)
    def is_adult(self):
        return self.age >= 18

    # Метод для вітання
    def greet(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років і я працюю як {self.job}.")

    # Метод зміни професії
    def change_job(self, new_job):
        old_job = self.job                     # Зберігаємо стару професію
        self.job = new_job                     # Змінюємо на нову
        print(f"{self.name} змінив(ла) роботу: з '{old_job}' на '{self.job}'.")

        # Якщо зміна різко відрізняється — попередження
        if self.is_radical_change(old_job, new_job):
            print("⚠️ Це серйозна зміна кар'єри!")

    # Метод, що додає 1 до віку (день народження)
    def birthday(self):
        self.age += 1
        print(f"🎉 З Днем народження, {self.name}! Тобі тепер {self.age} роки(ів).")

    # Внутрішній метод, що визначає радикальну зміну професії
    def is_radical_change(self, old, new):
        # Це список пар "дуже різних професій"
        radical_pairs = [
            ("Data Scientist", "Флорист"),
            ("AI Інженер", "Пекар"),
            ("Python Developer", "Бармен"),
            ("ML розробник-аматор", "Мандрівник")
        ]
        # Якщо старе й нове входять до пар — повертає True
        return (old, new) in radical_pairs or (new, old) in radical_pairs


# Клас Student наслідує (успадковує) все від класу Person
class Student(Person):
    # Додаємо новий параметр — університет
    def __init__(self, name, age, job, university):
        super().__init__(name, age, job)     # Викликаємо конструктор батьківського класу
        self.university = university         # Додаємо нову властивість: університет

    # Перевизначаємо метод display_info (додаємо вивід університету)
    def display_info(self):
        super().display_info()  # Використовуємо метод батьківського класу
        print(f"Навчається в університеті: {self.university}")

    # Перевизначаємо метод greet для студента
    def greet(self):
        print(f"Привіт! Я студент {self.name}, мені {self.age} років, я вчуся в {self.university} і працюю як {self.job}.")


# 🧪 ТЕСТУВАННЯ ВСЬОГО НА ПРАКТИЦІ

# Створюємо об'єкт Кулєбяки
kul = Person("Кулєбяка", 22, "ML розробник-аматор")
kul.greet()                     # Виводимо привітання
kul.birthday()                 # Симулюємо день народження
kul.change_job("Мандрівник")   # Зміна професії (радикально!)
kul.display_info()             # Показуємо всю оновлену інформацію

print("\n--- Студент ---")  # Роздільник

# Створюємо об'єкт студента
s1 = Student("Аліна", 19, "Python Developer", "КПІ")
s1.greet()             # Привітання студента
s1.display_info()      # Інформація про студента

# 🧪 ТЕСТУВАННЯ ВСЬОГО НА ПРАКТИЦІ

# Створюємо об'єкт Кулєбяки
kulebiaka = Person("Кулєбяка", 22, "ML розробник-аматор")
kulebiaka.greet()                     # Виводимо привітання
kulebiaka.birthday()                 # Симулюємо день народження
kulebiaka.change_job("Мандрівник")   # Зміна професії (радикально!)
kulebiaka.display_info()             # Показуємо всю оновлену інформацію

print("\n--- Студент ---")  # Роздільник

# Створюємо об'єкт студентки Аліни
alina = Student("Аліна", 19, "Python Developer", "КПІ")
alina.greet()             # Привітання студентки
alina.display_info()      # Інформація про студентку

print("\n--- Додаткові персонажі ---")  # Роздільник

# Створюємо об'єкт Семена
semen = Person("Семен", 35, "Бармен")
semen.greet()
semen.display_info()

# Створюємо об'єкт Марка
marko = Student("Марко", 21, "Флорист", "Львівська політехніка")
marko.greet()
marko.display_info()
print("\n---------------\n---------------Оновлений код-----\n>")




# ОНОВЛЕНИЙ КОД (ДОДАТКИ ДО ПОПЕРЕДНЬОГО)
# Клас Person — базовий клас для людей
class Person:
    count = 0  # Лічильник створених людей

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        self.friends = []  # Список друзів
        Person.count += 1

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job}")

    def is_adult(self):
        return self.age >= 18

    def greet(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років і я працюю як {self.job}.")

    def change_job(self, new_job):
        old_job = self.job
        self.job = new_job
        print(f"{self.name} змінив(ла) роботу: з '{old_job}' на '{self.job}'.")
        if self.is_radical_change(old_job, new_job):
            print("⚠️ Це серйозна зміна кар'єри!")

    def birthday(self):
        self.age += 1
        print(f"🎉 З Днем народження, {self.name}! Тобі тепер {self.age} років.")

    def is_radical_change(self, old, new):
        radical_pairs = [
            ("Data Scientist", "Флорист"),
            ("AI Інженер", "Пекар"),
            ("Python Developer", "Бармен"),
            ("ML розробник-аматор", "Мандрівник")
        ]
        return (old, new) in radical_pairs or (new, old) in radical_pairs

    def years_to_retirement(self):
        pension_age = 60
        if self.age >= pension_age:
            print(f"{self.name} вже на пенсії.")
        else:
            years_left = pension_age - self.age
            print(f"{self.name} до пенсії залишилось {years_left} років.")

    def compare_age(self, other_person):
        if self.age > other_person.age:
            print(f"{self.name} старший за {other_person.name}")
        elif self.age < other_person.age:
            print(f"{self.name} молодший за {other_person.name}")
        else:
            print(f"{self.name} та {other_person.name} однолітки")

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"{self.name} подружився з {friend.name}")


# Клас Student успадковує Person
class Student(Person):
    def __init__(self, name, age, job, university):
        super().__init__(name, age, job)
        self.university = university

    def display_info(self):
        super().display_info()
        print(f"Навчається в університеті: {self.university}")

    def greet(self):
        print(f"Привіт! Я студент {self.name}, мені {self.age} років, я вчуся в {self.university} і працюю як {self.job}.")


# 🧪 ТЕСТУВАННЯ

# Список усіх людей
all_people = []

# Створюємо об'єкти
kul = Person("Кулєбяка", 22, "ML розробник-аматор")
marko = Person("Марко", 45, "AI Інженер")
semen = Person("Семен", 61, "Садівник")
alina = Student("Аліна", 19, "Python Developer", "КПІ")

# Додаємо до загального списку
all_people.extend([kul, marko, semen, alina])

# Дії з об'єктами
kul.greet()
kul.birthday()
kul.change_job("Мандрівник")
kul.display_info()
kul.years_to_retirement()

print("\n--- Інші ---")

marko.greet()
semen.greet()
alina.greet()

print("\n--- Порівняння віку ---")
kul.compare_age(alina)
kul.compare_age(semen)

print("\n--- Дружба ---")
kul.add_friend(marko)
marko.add_friend(alina)

print("\n--- Всі люди ---")
for person in all_people:
    print("—" * 30)
    person.display_info()

print(f"\n🔢 Загалом створено людей: {Person.count}")
