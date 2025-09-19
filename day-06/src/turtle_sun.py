# Приветствую! ヽ（≧w≦）ノ

import turtle

PEN_COLOR = 'red'
FILL_COLOR = 'yellow'


def sun(t: turtle.Turtle):
    t.color(PEN_COLOR, FILL_COLOR)
    t.begin_fill()

    while True:
        t.forward(200)
        t.left(170)

        if abs(t.pos()) < 1:
            break

    t.end_fill()


def main():
    '''
    Главная функция, которая отрисовывает солнце.
    '''
    t = turtle.Turtle()
    t.shape('turtle')

    sun(t)

    t.ht()
    turtle.done()


if __name__ == '__main__':
    main()
