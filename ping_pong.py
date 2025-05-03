from pygame import *
from random import randint
from math import *
finish = False
run = True
clock = time.Clock()
FPS = 60
speed = 5
speed_ball_y = 5
speed_ball_x = 5
font.init()
font1 = font.SysFont('Arial', 60)
win1 = font1.render('PLAYER 1 WIN', True, (0, 0, 0))
win2 = font1.render('PLAYER 2 WIN', True, (0, 0, 0))
# создаем спрайты
class GameSprite(sprite.Sprite):
 # конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       # Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 # метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
# метод для управления спрайтом стрелками клавиатуры
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
#back = '5944b9d6fa912e5fba3b426a07c5513a.jpg'
back = (255,255,255)
p1 = Player('71bbfiBOi3L._AC_UL800_QL65_.jpg',30,250,50,100,speed)
p2 = Player('71bbfiBOi3L._AC_UL800_QL65_.jpg',620,250,50,100,speed)
ball = GameSprite('imgbin-table-tennis-racket-sport-blue-table-tennis-bat-9edAbv5MmWymJ8tgZLUUN47qx.jpg',325,250,50,50,speed)
window = display.set_mode((win_width, win_height))
#background = transform.scale(image.load(back), (win_width, win_height))
window.fill(back)
display.set_caption("Ping_Pong")










while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        # обновляем фон
        window.fill(back)
        #window.blit(background,(0,0))
        p1.update_left()
        p2.update_right()
        if ball.rect.y >= win_height - 40 or ball.rect.y <= 0:
            speed_ball_y = abs(speed_ball_y + 0.25)
            speed_ball_y *= -1
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y
        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            speed_ball_x = abs(speed_ball_x + 0.25)
            speed_ball_x *= -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(win2, (200, 200))
        if ball.rect.x >= win_width:
            finish = True
            window.blit(win1, (200, 200))



        p1.reset()
        p2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
