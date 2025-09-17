import random

def guess_number():
    '''
    Игра "Угадай число" от 1 до 100 с подсчетом попыток.
    '''
    target = random.randint(1, 100)
    attempts = 0
    print('Я загадал число от 1 до 100. Попробуй угадать!')
    
    while True:
        guess = int(input('Твоя догадка: '))
        attempts += 1
        if guess < target:
            print('Больше!')
        elif guess > target:
            print('Меньше!')
        else:
            print(f'Поздравляю! Угадал за {attempts} попыток.')
            break

      
if __name__ == '__main__':
    guess_number()