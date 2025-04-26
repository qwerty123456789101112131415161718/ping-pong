from pygame import *
from random import randint
finish = False
run = True
clock = time.Clock()
FPS = 60
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
    def update_upper(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_downer(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
win_width = 700
win_height = 500
back = '5944b9d6fa912e5fba3b426a07c5513a.jpg'
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(back), (win_width, win_height))
display.set_caption("Ping_Pong")










while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
    display.update()
    clock.tick(FPS)
