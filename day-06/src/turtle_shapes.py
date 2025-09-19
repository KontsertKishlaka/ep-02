# Приветствую! ヽ（≧w≦）ノ

import turtle
import os


def clear_screen():
    '''
    Очищает консоль.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def setup_turtle() -> turtle.Turtle:
    '''
    Настраивает конфиг черепашки.
    '''
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(5)
    t.width(3)
    
    return t


def clear_canvas(t: turtle.Turtle):
    '''
    Очищает холст и возвращает черепашку в начальное положение.
    '''
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)  # Сброс направления
    t.st()


def draw_square(t: turtle.Turtle, size=100, fill_color='red'):
    '''
    Рисует квадрат.
    '''
    t.color('black', fill_color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.ht()


def draw_rectangle(t: turtle.Turtle, width=150, height=75, fill_color='blue'):
    '''
    Рисует прямоугольник.
    '''
    t.color('black', fill_color)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        
    t.end_fill()
    t.ht()


def draw_circle(t: turtle.Turtle, radius=50, fill_color='green'):
    '''
    Рисует круг.
    '''
    t.color('black', fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.ht()


def draw_triangle(t: turtle.Turtle, size=100, fill_color='orange'):
    '''
    Рисует равносторонний треугольник.
    '''
    t.color('black', fill_color)
    t.begin_fill()
    
    for _ in range(3):
        t.forward(size)
        t.left(120)
        
    t.end_fill()
    t.ht()


def show_menu():
    '''
    Отображает меню выбора фигур.
    '''
    print('\n🎨 ВЫБЕРИТЕ ФИГУРУ ДЛЯ ОТРИСОВКИ 🎨\n')
    print('1 - Квадрат')
    print('2 - Прямоугольник')
    print('3 - Круг')
    print('4 - Треугольник')
    print('q - Выйти из программы\n')


def main():
    '''
    Главная функция, которая отрисовывает фигуру по выбору
    '''
    # Настройка экрана
    screen = turtle.Screen()
    screen.title('Рисование фигур с Turtle')
    screen.bgcolor('white')

    # Конфиг черепашки
    t = setup_turtle()

    while True:
        clear_screen()
        show_menu()

        choice = input('Ваш выбор: ').strip().lower()

        if choice == 'q':
            print('До свидания! 👋')
            break

        clear_canvas(t)

        if choice == '1':
            print('Рисую квадрат...')
            draw_square(t, fill_color='lightcoral')
        elif choice == '2':
            print('Рисую прямоугольник...')
            draw_rectangle(t, fill_color='lightblue')
        elif choice == '3':
            print('Рисую круг...')
            draw_circle(t, fill_color='lightgreen')
        elif choice == '4':
            print('Рисую треугольник...')
            draw_triangle(t, fill_color='gold')
        else:
            print('❌ Неверный выбор! Попробуйте снова.')
            input('Нажмите Enter для продолжения...')
            continue

        print('Фигура нарисована! ✅')
        input('Нажмите Enter для возврата в меню...')

    screen.bye()


if __name__ == '__main__':
    main()
