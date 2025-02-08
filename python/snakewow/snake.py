######引用数据库与函数######

from turtle import *

from gamespace import square
from random import randrange
from time import sleep
######定义变量######
snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
apple_x=randrange(-20,18)*10
apple_y=randrange(-19,19)*10
aim_x=0
aim_y=10
score=6
max_score=6
######定义函数######
def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y
def inside():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False
def inside_snake():
    for n in range(len(snake)-1):
        if snake[n][0]==snake[-1][0] and snake[n][1]==snake[-1][1]:
            return False
    return True
def gameLoop():
    global apple_x, apple_y, aim_x, aim_y, snake, score,max_score
    n = 0
    snake.append([snake[-1][0] + aim_x, snake[-1][1] + aim_y])
    # print(snake[-1][0],snake[-1][1])

    if snake[-1][0] != apple_x or snake[-1][1] != apple_y:
        snake.pop(0)
    else:
        apple_x = randrange(-20, 18) * 10
        apple_y = randrange(-19, 19) * 10
        score += 1
    if (not inside()) or not inside_snake():
        square(snake[-1][0], snake[-1][1], 10, "red")
        update()
        snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
        apple_x = randrange(-20, 18) * 10
        apple_y = randrange(-19, 19) * 10
        aim_x = 0
        aim_y = 10
        
        if(score>max_score):
            max_score=score
        penup()
        goto(0, 0)
        pendown()
        write(f"Game Over! score={score}\n   maxscore={max_score}", align="center", font=("Arial", 30, "normal"))
        hideturtle()
        down()
        score = 6
        update()
        sleep(2)
    clear()
    square(-210, -200, 410, "black")
    square(-200, -190, 390, "white")
    square(apple_x, apple_y, 10, "red")
    for n in range(len(snake)):
        square(snake[n][0], snake[n][1], 10, "black")

    ontimer(gameLoop, 300)
    update()
######主程序######
setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda :change(0,10),"w")
onkey(lambda :change(0,-10),"s")
onkey(lambda :change(-10,0),"a")
onkey(lambda :change(10,0),"d")
gameLoop()
done()