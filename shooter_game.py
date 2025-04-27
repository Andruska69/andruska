#Создай собственный Шутер!

from pygame import *
from random import randint
window = display.set_mode((700,500))
background = transform.scale(image.load('galaxy.jpg'),(700, 500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_wiz,player_hi, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_wiz,player_hi))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x <  630:
            self.rect.x += self.speed
    def fire(self):
        bullit = Bullit('bullet.png',self.rect.centerx,self.rect.top,15,30,15)
        bullits.add(bullit)

sprite1 = Player('rocket.png', 310,435,65, 65, 10)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0,700)


class Bullit(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y  <= 0:
            self.kill()

Enemy1 = Enemy('ufo.png',100,0,65, 65, 5)
Enemy2 = Enemy('ufo.png',200,0,65, 65, 5)
Enemy3 = Enemy('ufo.png',300,0,65, 65, 5)
Enemy4 = Enemy('ufo.png',400,0,65, 65, 5)
Enemy5 = Enemy('ufo.png',500,0,65, 65, 5)

monsters = sprite.Group()
monsters.add(Enemy1)
monsters.add(Enemy2)
monsters.add(Enemy3)
monsters.add(Enemy4)
monsters.add(Enemy5)

bullits = sprite.Group()
run = True
while run:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                sprite1.fire()
    sprite1.reset()
    sprite1.update()
    monsters.draw(window)
    monsters.update()
    bullits.draw(window)
    bullits.update()
    display.update()
    sprites_list = sprite.groupcollide(monsters, bullits, True, True)
    for a in sprites_list: 

        Enemy1 = Enemy('ufo.png',randint(0,600),0,65, 65, 5)
        monsters.add(Enemy1)


