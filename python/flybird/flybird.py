import pygame
from random import randrange
from time import sleep

pygame.init()

#######定义变量#######
map_width = 284
map_height = 512
frame = 0
FPS = 60
pipes = [[180, 4]]
bird = [40, map_height // 2 - 50]
gamescreen = pygame.display.set_mode((map_width, map_height))
clock = pygame.time.Clock()
bird_wing_up = bird_wing_up_copy = pygame.image.load("images/bird_wing_up.png")
bird_wing_down = bird_wing_down_copy = pygame.image.load("images/bird_wing_down.png")
background = pygame.image.load("images/background.png")
pipe_body = pygame.image.load("images/pipe_body.png")
pipe_end = pygame.image.load("images/pipe_end.png")
grativity = 0.2
velocity = 0
score = 0  # 计分
max_score = 0  # 最高分

#######定义函数#######
def safe():
    if bird[1] < 0:
        print("hit ceiling")
    if bird[1] > map_height - 35:
        print("hit floor")
    if pipes[0][0] - 28 < bird[0] < pipes[0][0] + 77:
        if bird[1] < (pipes[0][1] + 1) * 32-5 or bird[1] > (pipes[0][1] + 4) * 32+5:
            print("hit pipe")
            return False
    return True

def reset():
    global pipes, bird, frame, velocity, grativity, map_height, map_width, score, max_score
    pipes.clear()
    bird.clear()
    pipes = [[180, 4]]
    bird = [40, map_height // 2 - 50]
    frame = 0
    velocity = 0
    grativity = 0.2
    map_width = 284
    map_height = 512
    if score > max_score:
        max_score = score  # 更新最高分
    score = 0  # 重置分数

def drawPipes():
    global pipes
    for n in range(len(pipes)):
        for m in range(0, pipes[n][1]):
            gamescreen.blit(pipe_body, (pipes[n][0], m * 32))
        for m in range(pipes[n][1] + 6, 16):
            gamescreen.blit(pipe_body, (pipes[n][0], m * 32))
        gamescreen.blit(pipe_end, (pipes[n][0], (pipes[n][1]) * 32))
        gamescreen.blit(pipe_end, (pipes[n][0], (pipes[n][1] + 5) * 32))
        pipes[n][0] -= 1

def drawBird(x, y):
    global frame
    if 0 <= frame <= 30:
        gamescreen.blit(bird_wing_up, (x, y))
        frame += 1
    elif 30 < frame <= 60:
        gamescreen.blit(bird_wing_down, (x, y))
        frame += 1
        if frame == 60:
            frame = 0

def drawScore():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    gamescreen.blit(text, (10, 10))
    text = font.render(f"Max Score: {max_score}", True, (255, 255, 255))
    gamescreen.blit(text, (10, 50))

def gameLoop():
    global pipes, bird, grativity, velocity, bird_wing_up, bird_wing_down, score
    while True:
        if len(pipes) < 4:
            x = pipes[-1][0] + 200
            open_pos = randrange(1, 9)
            pipes.append([x, open_pos])
        if pipes[0][0] < -100:
            pipes.pop(0)
            score += 1  # 每次通过一个圆筒积一分

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                bird[1] -= 40
                velocity = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        gamescreen.blit(background, (0, 0))
        velocity += grativity
        bird[1] += velocity
        bird_wing_down = pygame.transform.rotate(bird_wing_down_copy, -90 * (velocity / 15))
        bird_wing_up = pygame.transform.rotate(bird_wing_up_copy, -90 * (velocity / 15))
        drawBird(bird[0], bird[1])
        drawPipes()
        drawScore()  # 显示分数
        pygame.display.update()
        if not safe():
            print("Game Over")  # 输出 "Game Over"
            sleep(1)
            reset()
        clock.tick(FPS)

#######主程序#######
gameLoop()