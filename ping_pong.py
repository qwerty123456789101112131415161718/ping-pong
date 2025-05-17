
from pygame import *
from random import randint
from math import *

finish = False
run = True
rand = 0
rand2 = 0
clock = time.Clock()
FPS = 60
speed = 5
lifes1 = 3
lifes2 = 3

rand = randint(1,2)
if rand==1:
    speed_ball_y = 5
elif rand == 2:
    speed_ball_y = -5
rand2 = randint(1,2)
if rand2==1:
    speed_ball_x = 5
elif rand2 == 2: 
    speed_ball_x = -5

font.init()
font1 = font.SysFont('Arial', 40)
win1 = font1.render('PLAYER 1 WIN', True, (0, 0, 0))
win2 = font1.render('PLAYER 2 WIN', True, (0, 0, 0))

# Создаем спрайты
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def start(self):  # Метод для установки начального положения
        self.rect.x = 325
        self.rect.y = 250


class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
back = (255,255,255)
p1 = Player('71bbfiBOi3L._AC_UL800_QL65_.jpg',10,250,20,100,speed)
p2 = Player('71bbfiBOi3L._AC_UL800_QL65_.jpg',670,250,20,100,speed)
ball = GameSprite('imgbin-table-tennis-racket-sport-blue-table-tennis-bat-9edAbv5MmWymJ8tgZLUUN47qx.jpg',325,250,50,50,speed)
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption("Ping_Pong")

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(back)
        p1.update_left()
        p2.update_right()
        if ball.rect.y >= win_height - 40 or ball.rect.y <= 0:
            speed_ball_y /= 0.95
            speed_ball_y *= -1
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y
        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            speed_ball_x /= 0.95
            speed_ball_x *= -1
        if ball.rect.x <= 0:
            lifes1 -= 1
            if lifes1 == 0:
                finish = True
                window.blit(win2, (200, 200))
            else:
                ball.start()  # Вернуть мяч в центр
                speed_ball_x *= -1
                speed_ball_y *= -1
        elif ball.rect.x >= win_width:
            lifes2 -= 1
            if lifes2 == 0:
                finish = True
                window.blit(win1, (200, 200))
            else:
                ball.start()  # Вернуть мяч в центр
                speed_ball_x *= -1
                speed_ball_y *= -1
                
        life1 = font1.render("Жизни: " + str(lifes1), 1, (0, 0, 0,))
        window.blit(life1, (30, 10))
        life2 = font1.render("Жизни: " + str(lifes2), 1, (0, 0, 0,))
        window.blit(life2, (550, 10))
        p1.reset()
        p2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
