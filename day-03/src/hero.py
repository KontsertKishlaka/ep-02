# Приветствую! ヽ（≧w≦）ノ

def create_hero():
    '''
    Создание персонажа с выбором расы и повышением характеристик по уровням.
    '''
    print('Добро пожаловать в мир магии и приключений!')
    name = input('Как зовут твоего героя? ')
    races = ['эльф', 'гном', 'человек', 'хоббит']
    
    print(f'Я рад видеть тебя, {name}! К какому виду ты принадлежишь: {races}?')
    
    hp = 0
    damage = 0
    chosen_race = input('Твой выбор: ').lower()
    
    if chosen_race == 'эльф':
        hp, damage = 80, 15
    elif chosen_race == 'гном':
        hp, damage = 100, 12
    elif chosen_race == 'человек':
        hp, damage = 90, 14
    elif chosen_race == 'хоббит':
        hp, damage = 70, 10
    else:
        print('Неизвестная раса! Установлены стандартные характеристики.')
        hp, damage = 50, 5
    
    print(f'\nТвой герой: {name}')
    print(f'Раса: {chosen_race}')
    print(f'Здоровье: {hp}')
    print(f'Урон: {damage}')
    
    levels = [1, 2, 3, 4, 5]
    for level in levels:
        hp += 10
        damage += 2
        print(f'Уровень {level}: HP={hp}, Урон={damage}')

if __name__ == '__main__':
    create_hero()