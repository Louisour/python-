import random

import pygame
import time
import pygame
from pygame.constants import *



class Heroplane(object):
    def __init__(self,screen):
        self.player = pygame.image.load('images/me1.png')
        self.screen = screen
        self.x = 480 / 2 - 102 / 2
        self.y = 550

        # 飞机速度
        self.speed = 10
        #子弹列表
        self.bullets=[]
    def key_control(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:

            self.y -= self.speed
        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:

            self.y += self.speed
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:

            self.x += self.speed
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:

            self.x -= self.speed
        if key_pressed[pygame.K_SPACE]:
            #发射子弹
            bullet=Bullet(self.screen,self.x,self.y,self.speed)
            self.bullets.append(bullet)
    def display(self):
        # 3将飞机图片贴到窗口
        self.screen.blit(self.player, (self.x, self.y))
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()

class Enemyplane(object):
    def __init__(self,screen):
        self.player = pygame.image.load('images/enemy1.png')#57*43
        self.screen = screen
        self.x = 0
        self.y = 0

        # 飞机速度
        self.speed = 15
        #子弹列表
        self.bullets=[]
        self.direction = 'right'
    def display(self):
        # 3将飞机图片贴到窗口
        self.screen.blit(self.player, (self.x, self.y))
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.x+=self.speed-10
        elif self.direction == 'left':
            self.x-=self.speed-10
        if self.x>480-57:
            self.direction = 'left'
        elif self.x<0:
            self.direction = 'right'
    def auto_fire(self):

        random_num=random.randint(1,10)
        if random_num == 8:
            bullet=EnemyBullet(self.screen,self.x,self.y,self.speed)
            self.bullets.append(bullet)
class Bullet(object):
    def __init__(self,screen,x,y,speed):
        self.x = x+102/2-5/2
        self.y = y-11
        self.image=pygame.image.load('images/bullet1.png')
        self.screen=screen
        self.speed=10
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def auto_move(self):
        self.y-=self.speed

class EnemyBullet(object):
    def __init__(self,screen,x,y,speed):
        self.x = x+56/2-5/2
        self.y = y+43
        self.image=pygame.image.load('images/bullet2.png')#5*11
        self.screen=screen
        self.speed=10
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def auto_move(self):
        self.y+=self.speed


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('sound/game_music.ogg')
        pygame.mixer.music.set_volume(0.5)
    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)



def main():#整个程序控制
    sound=GameSound()
    sound.playBackgroundMusic()
    #1窗口
    screen=pygame.display.set_mode((480,700), 0, 32)
    #2图片背景
    background = pygame.image.load('images/background.png')
    player = Heroplane(screen)
    enemyplane = Enemyplane(screen)
    while True:
        # 3将背景图片贴到窗口
        screen.blit(background, (0, 0))

        #获取事件
        for event in pygame.event.get():
            #判断事件类型
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        player.key_control()
        player.display()
        enemyplane.display()
        enemyplane.auto_move()
        enemyplane.auto_fire()


        #4show窗口内容
        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()

