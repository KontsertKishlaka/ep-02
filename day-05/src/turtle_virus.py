# Приветствую! ヽ（≧w≦）ノ

import turtle

PEN_COLOR = 'green'
BG_COLOR = 'black'


def virus(t: turtle.Turtle):
    '''
    Метод отрисовки вируса.
    '''
    t.speed(40)
    t.color(PEN_COLOR)
    b = 200

    while b > 0:
        t.left(b)
        t.forward(b*3)
        b = b - 1


def main():
    '''
    Главная функция, которая отрисовывает вирус.
    '''
    turtle.bgcolor(BG_COLOR)
    t = turtle.Turtle()
    t.shape('turtle')

    virus(t)

    t.ht()
    turtle.done()


if __name__ == '__main__':
    main()
