# Приветствую! ヽ（≧w≦）ノ

import os
import re


def calculate_average(*args) -> float:
    '''
    Задание №1: Среднее значение из переменного количества аргументов.
    '''
    numbers = [arg for arg in args if isinstance(arg, (int, float))]
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def reverse_words(sentence: str) -> str:
    '''
    Задание №2: Принимает строку и возвращает новую строку с обратным порядком слов.
    '''
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


def is_palindrome(text: str) -> bool:
    '''
    Задание №3: Проверяет, является ли строка палиндромом.
    '''
    cleaned_text = re.sub(r'[^\w]', '', text.lower())
    return cleaned_text == cleaned_text[::-1]


def find_longest_subsequence(str1: str, str2: str) -> str:
    '''
    Задание №4: Находит наибольшую общую подпоследовательность двух строк.
    '''
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Восстановление подпоследовательности
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            result.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


def main():
    '''
    Главная функция, запускает выполнение выбранного задания.
    '''
    while True:
        print('\nДоступные задания:')
        for i in range(1, 5):
            print(f'Задание №{i}')

        choice = input(
            '\nВведите номер задания для выполнения (или "q" для выхода): ').strip()
        os.system('cls')

        if choice == 'q':
            return

        if choice == '1':
            print(f'\n--- Задание №{choice} ---')
            print(calculate_average(1, 2, 3, 4, 5))
            print(calculate_average(1.5, 2.5, 'a', 3.5, 4.5))
            print(calculate_average(10, 20, 30, 40))
        elif choice == '2':
            print(f'\n--- Задание №{choice} ---')
            print(reverse_words('Hello world'))
            print(reverse_words('Python is awesome'))
            print(reverse_words('Привет мир'))
        elif choice == '3':
            print(f'\n--- Задание №{choice} ---')
            print(is_palindrome('A man, a plan, a canal: Panama'))
            print(is_palindrome('racecar'))
            print(is_palindrome('hello'))
            print(is_palindrome('А роза упала на лапу Азора'))
        elif choice == '4':
            print(f'\n--- Задание №{choice} ---')
            print(find_longest_subsequence('ABCDGH', 'AEDFHR'))
            print(find_longest_subsequence('AGGTAB', 'GXTXAYB'))
            print(find_longest_subsequence('abcde', 'ace'))
        elif choice == 'q':
            return
        else:
            print(f'\nЗадание №{choice} не найдено.')


if __name__ == '__main__':
    main()
