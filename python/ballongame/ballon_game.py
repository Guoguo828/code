from turtle import *
from gamespace import square, line
from random import randrange, choice
from time import sleep

##########定义变量##########
ballons = []
color_option = ["red", "blue", "light blue", "green", "yellow", "purple", "orange", "black", "dark blue", "pink", "orange", "light green"]
size = 50
score = 0
max_score = 0
game_over = False
d = choice(color_option)
time_left = 60  # 倒计时60秒
show_message = False  # 控制是否显示消息
num1 = 0

##########定义函数##########
def distance(a, b, x, y):
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5

def tap(x, y):
    global score, game_over, show_message, num1
    num1 = 0
    to_remove = []
    for n in range(len(ballons)):
        if distance(ballons[n][0], ballons[n][1], x, y) < size/2+5:
            if ballons[n][2] == d or ballons[n][2] == "black":
                game_over = True
                break
            to_remove.append(n)
            score += 1
            num1 += 1
    for n in sorted(to_remove, reverse=True):
        ballons.pop(n)
    if num1 > 1:
        show_message = True
        ontimer(clear_message, 1000)  # 1秒后清除消息

def clear_message():
    global show_message
    show_message = False

def draw():
    global score, max_score, game_over, time_left, show_message, num1
    clear()
    if show_message:
        penup()
        goto(0, 180)  # 定位到游戏框框最上端
        pendown()
        write(f"Good! {num1} ballons", align="center", font=("Arial", 20, "normal"))
    penup()
    goto(-200, 140)  # 定位到左上角
    pendown()
    color("black")  # 设置字体颜色为黑色

    if score > max_score:
        max_score = score
    write(f"score={score}\nmax_score={max_score}\ntime_left={time_left}", align="left", font=("Arial", 15, "normal"))
    for n in range(1, len(ballons) + 1):
        line(ballons[-n][0], ballons[-n][1], ballons[-n][0], ballons[-n][1] - size * 1.5, 2, ballons[-n][2])
        penup()
        goto(ballons[-n][0], ballons[-n][1])
        dot(size, ballons[-n][2])
        ballons[-n][1] = ballons[-n][1] + 1
    update()

    if game_over:
        penup()
        goto(0, 0)
        pendown()
        write("Game Over!", align="center", font=("Arial", 30, "normal"))
        hideturtle()
        update()
        sleep(1)
        reset_game()

def reset_game():
    global ballons, score, game_over, d, time_left
    ballons = []
    score = 0
    game_over = False
    d = choice(color_option)
    time_left = 60  # 重置倒计时
    ontimer(gameLoop, 500)  # 延迟重新开始游戏

def countdown():
    global time_left, game_over
    if time_left > 0:
        time_left -= 1
        ontimer(countdown, 1000)  # 每秒更新一次倒计时
    else:
        game_over = True

def gameLoop():
    if not game_over:
        if randrange(0, 50) == 1:
            x = randrange(-200 + size, 200 - size)
            c = choice(color_option)
            ballons.append([x, -200 - size, c])
        draw()
        ontimer(gameLoop, 5)
    else:
        draw()  # 确保在游戏结束时调用 draw 函数

##########主程序##########
setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onscreenclick(tap)
gameLoop()
countdown()  # 启动倒计时
done()