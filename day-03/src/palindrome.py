def check_palindrome():
    '''
    Проверка, является ли объединенная строка палиндромом.
    '''
    str1 = input('Введите первую строку: ')
    str2 = input('Введите вторую строку: ')
    combined = str1 + str2
    is_palindrome = combined == combined[::-1]
    
    print('Строка является палиндромом' if is_palindrome else 'Строка не является палиндромом')
    

if __name__ == '__main__':
    check_palindrome()