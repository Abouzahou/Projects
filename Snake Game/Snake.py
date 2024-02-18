from turtle import *
from random import randrange
from freegames import square, vector

snake = [vector(10, 0)]
view = vector(0, -10)
target = vector(0,0)

def change(x,y):
    view.x = x
    view.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    head.move(view)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return   

    snake.append(head)

    if head == target:
        print('Snake:', len(snake))
        target.x = randrange(-15, 15) * 10
        target.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(target.x, target.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()                

