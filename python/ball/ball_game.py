from random import random, choice, randint
from time import sleep
from turtle import *

##########定义变量##########
player = [0, -140]
ball = [0, 140]
direction = [choice([-2, -1, 1, 2]), choice([-2, -1])]
block = [randint(-290, 290), randint(-130, 130)]  # 随机位置的小方块
score = 0  # 计分
max_score = 0  # 最高分
block_timer = 0  # 方块存在时间计时器
game_timer = 0  # 游戏计时器
total_time = 180  # 总时间180秒

##########定义函数##########
def move(aim):
    player[0] += aim

def square(x, y, size):
    up()
    goto(x, y)
    down()
    fillcolor("blue")
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()

def bounce():
    if ball[0] >= 300 or ball[0] <= -290:
        direction[0] = -direction[0]
    if ball[1] >= 150:
        direction[1] = -direction[1]
    if ball[1] <= -140 + 15 and player[0] <= ball[0] <= player[0] + 70:
        direction[1] = -direction[1]

def outside():
    return ball[1] <= -145

def hit_block():
    return abs(ball[0] - block[0]) < 15 and abs(ball[1] - block[1]) < 15

def draw():
    clear()
    # 绘制黑色边框
    rectangle(-310, 160, 620, 320, "black")
    # 绘制白色背景
    rectangle(-305, 155, 610, 310, "white")
    
    up()
    goto(ball[0], ball[1])
    dot(10, "red")
    rectangle(player[0], player[1], 70, 10, "black")
    square(block[0], block[1], 10)  # 绘制小方块
    penup()
    goto(-290, 80)  # 定位到左上角
    pendown()
    remaining_time = total_time - game_timer  # 计算剩余时间
    write(f"Score: {score}\n最高分: {max_score}\nTime: {remaining_time}s", align="left", font=("Arial", 15, "normal"))  # 显示分数和剩余时间
    update()

def countdown():
    global game_timer
    if game_timer < total_time:
        game_timer += 1
        ontimer(countdown, 1000)  # 每秒更新一次倒计时

def gameloop():
    global score, block_timer, game_timer, max_score
    bounce()
    ball[0] += direction[0] * 3
    ball[1] += direction[1] * 3
    if score > max_score:
        max_score = score
    if hit_block():
        block[0] = randint(-290, 290)
        block[1] = randint(-130, 130)
        score += 1  # 击中方块加一分
        block_timer = 0  # 重置方块计时器
    draw()
    if outside() or game_timer >= total_time:
        penup()
        goto(0, 0)
        pendown()
        write("Game Over!", align="center", font=("Arial", 30, "normal"))
        hideturtle()
        update()
        ontimer(reset_game, 2000)  # 2秒后重置游戏
        return
    block_timer += 1
    if block_timer >= 300:  # 15秒（300个50毫秒）
        block[0] = randint(-290, 290)
        block[1] = randint(-130, 130)
        block_timer = 0  # 重置方块计时器
    ontimer(gameloop, 50)

def reset_game():
    global ball, direction, score, block_timer, game_timer
    ball = [0, 140]
    direction = [choice([-2, -1, 1, 2]), choice([-2, -1])]
    score = 0  # 重置分数
    block_timer = 0  # 重置方块计时器
    game_timer = 0  # 重置游戏计时器
    gameloop()

def rectangle(x, y, w, h, color_name):
    up()
    goto(x, y)
    down()
    fillcolor(color_name)
    begin_fill()
    for i in range(2):
        forward(w)
        right(90)
        forward(h)
        right(90)
    end_fill()

##########主程序##########
setup(620, 320, 0, 0)
hideturtle()
tracer(False)
countdown()
listen()
onkey(lambda: move(20), "d")
onkey(lambda: move(-20), "a")
gameloop()
done()