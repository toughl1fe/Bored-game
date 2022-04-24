from pygame import *
from random import randint
# Образец класса
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width=50, player_high=50 ):
        super().__init__()        
        self.image = transform.scale(image.load(player_image),(player_width, player_high))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self. image, (self.rect.x, self.rect.y))
# Класс игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.x < 730:
            self.rect.x += self.speed
# Класс игрока 2
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 730:
            self.rect.x += self.speed
        
# Класс мяча
class Ball(GameSprite):
    def update(self):
        pass  
# Создание окна и счетчик кадров в секунду
window = display.set_mode((900, 700))
display.set_caption('Bored game')
background = transform.scale(image.load('background.jpg'),(800, 600))
FPS = 160
# Создание всех персонажей
player = Player('racket2.jpg',10,5,5)
player2 = Player2('racket2.jpg',895,5,5)
ball = Ball('шаринган.jpg',50,1,1)


# Причины остановки игры и показание всех персонажей
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

display.update()
Clock.tick(FPS)


