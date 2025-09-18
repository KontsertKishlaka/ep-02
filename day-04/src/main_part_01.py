# Приветствую! ヽ（≧w≦）ノ

import calendar
import os


def task1():
    '''
    Задание №1: Вывод степеней числа 2.
    '''
    n = 10
    powers = list(map(lambda x: 2 ** x, range(1, n + 1)))
    print(powers)


def task2():
    '''
    Задание №2: Поиск чисел, кратных 13, в списке.
    '''
    numbers = [13, 26, 5, 39, 50, 65]
    multiples = list(filter(lambda x: x % 13 == 0, numbers))
    print(multiples)


def task3():
    '''
    Задание №3: Калькулятор с функциями.
    '''
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('Ошибка: Деление на ноль.')

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    try:
        a = float(input('Введите первое число: '))
        op = input('Введите операцию (+, -, *, /): ')
        b = float(input('Введите второе число: '))
        result = operations.get(op, lambda x, y: 'Неизвестная операция')(a, b)
        print(f'Результат: {result}')
    except ValueError:
        print('Ошибка: введите числа.')


def task4():
    '''
    Задание №4: Вывод календаря.
    '''
    year = int(input('Введите год: '))
    month = input('Введите месяц (например, январь): ').lower()
    months = {
        'январь': 1,
        'февраль': 2,
        'март': 3,
        'апрель': 4,
        'май': 5,
        'июнь': 6,
        'июль': 7,
        'август': 8,
        'сентябрь': 9,
        'октябрь': 10,
        'ноябрь': 11,
        'декабрь': 12
    }
    if month not in months:
        print('Неверный месяц.')
        return
    print(calendar.month(year, months[month]))


def task5():
    '''
    Задание №5: Таблица умножения для чисел 4, 7, 9.
    '''
    for num in [4, 7, 9]:
        print(f'Таблица умножения для {num}:')
        for i in range(1, 11):
            print(f'{num} * {i} = {num * i}')
        print()


def task6():
    '''
    Задание №6: Вычисление площади окружности.
    '''
    def calculate_area(radius, pi=3.14):
        return pi * (radius ** 2)

    print(calculate_area(5))
    print(calculate_area(3, 3.14159))


def task7():
    '''
    Задание №7: Среднее арифметическое списка чисел.
    '''
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

    print(calculate_average([1, 2, 3, 4, 5]))
    print(calculate_average([10, 20, 30]))


def task8():
    '''
    Задание №8: Валидация: число простое.
    '''
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    print(is_prime(7))
    print(is_prime(10))


def task9():
    '''
    Задание №9: Поиск палиндромов в списке.
    '''
    def find_palindromes(words):
        return [word for word in words if word == word[::-1]]

    words = ['радар', 'мир', 'топот', 'комок', 'python']
    print(find_palindromes(words))


def main():
    '''
    Главная функция, запускает выполнение выбранного задания.
    '''
    tasks = {
        '1': task1,
        '2': task2,
        '3': task3,
        '4': task4,
        '5': task5,
        '6': task6,
        '7': task7,
        '8': task8,
        '9': task9
    }

    while True:
        print('\nДоступные задания:')
        for key in tasks:
            print(f'Задание №{key}')

        choice = input(
            '\nВведите номер задания для выполнения (или "q" для выхода): ').strip()
        os.system('cls')

        if choice == 'q':
            return

        selected_task = tasks.get(choice)
        if selected_task:
            print(f'\n--- Задание №{choice} ---')
            selected_task()
        else:
            print(f'\nЗадание №{choice} не найдено.')


if __name__ == '__main__':
    main()
