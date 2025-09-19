# Приветствую! ヽ（≧w≦）ノ

import turtle

BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'


def body(t: turtle.Turtle):
    '''
    Отрисовывает тело амогуса.
    '''
    t.pensize(30)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    # Сторона справа
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # Голова
    t.right(180)
    t.circle(100, -180)

    # Сторона слева
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def glass(t: turtle.Turtle):
    '''
    Отрисовывает очки амогуса.
    '''
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()

    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()


def backpack(t: turtle.Turtle):
    '''
    Отрисовывает рюкзак амогуса.
    '''
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)
    t.end_fill()


def main():
    '''
    Главная функция, которая отрисовывает амогуса.
    '''
    t = turtle.Turtle()
    t.shape('turtle')

    body(t)
    glass(t)
    backpack(t)

    t.ht()
    turtle.done()


if __name__ == '__main__':
    main()
