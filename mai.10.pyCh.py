square = lambda x: x ** 2
print(square(5))  # Виведе: 25


def square(x):
    return x ** 2
print(square(5))


sum_numbers = lambda x, y: x + y
print(sum_numbers(3, 7))  # Виведе: 10


people = [("Кулєбяка", 34), ("Олег", 28), ("Марина", 25)]
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)
# Відсортує за віком: [('Марина', 25), ('Олег', 28), ('Кулєбяка', 34)]


check_point = lambda x: x%5 == 0
print(check_point(9))
print(check_point(16))

max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # 20
print(max_num(50, 30))  # 50


starts_with_A = lambda s: s[-1].lower() == 'a'
print(starts_with_A("Apple"))  # True
print(starts_with_A("Banana"))  # False

concat = lambda s1, s2: s1 + " " + s2
print(concat("Hello", "World"))  # Hello World
print(concat("Кулєбяка", "топ"))  # Кулєбяка топ

plus_num = lambda a: a > 0
print(plus_num(10))
print(plus_num(-50))

last_letter = lambda s: s[-1] if s else None
print(last_letter("Python"))  # n
print(last_letter(""))        # None


modulo = lambda a, b: a % b
print(modulo(10, 3))  # 1
print(modulo(20, 7))  # 6

found_word = lambda s: "Python" in s
print(found_word("My Dear Python, I love you"))
print(found_word("Anybody Home?"))


square = lambda x: x ** 2
print(square(8))

capitalize_word = lambda s: s.title()
print(capitalize_word("я вітаю вас шановні пані та панове у нашому славетному місті харків"))  # Hello
print(capitalize_word("шо ви пацики на моцику з повним баком бензіка?"))  # Кулєбяка
