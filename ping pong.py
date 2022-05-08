from pygame import *
from random import randint
# Образец класса
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_high):
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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
# Класс игрока 2
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
        
# Класс мяча
class Ball(GameSprite):
    def update(self):
        pass  
# Создание окна и счетчик кадров в секунду
window = display.set_mode((800, 600))
display.set_caption('Bored game')
background = transform.scale(image.load('background.png'),(800, 600))

FPS = 160
# Создание всех персонажей
player = Player('Rackets3.jpg',5,5,5, 50, 100)
player2 = Player2('Rackets3.jpg',750,5,5, 50, 100)
ball = Ball('pong3.png',375,275,1, 50, 50)


# Причины остановки игры и показание всех персонажей
speed_y = 3
speed_x = 3
finish = False
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 600 - 50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    window.blit(background, (0,0))
    player.reset()
    player.update()
    player2.reset()
    player2.update()
    ball.reset()
    ball.update()
    

    display.update()
    clock.tick(FPS)


