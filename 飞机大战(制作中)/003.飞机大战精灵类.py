import random
import time
import pygame
from pygame.constants import *


#现在开始继承精灵类，精灵类可以实现碰撞检测，除此之外还有一些方便的功能，等待学习
class Heroplane(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)#精灵类的初始化方法必用；
        self.player = pygame.image.load('./images/me1.png')
        self.rect=self.player.get_rect()#这里的rect指矩形，也就是通过图像间的矩形对象来判断是否碰撞
        self.rect.topleft=[480 / 2 - 102 / 2,550]#飞机图片的左上角坐标
        self.screen = screen
        # 飞机速度
        self.speed = 10
        #子弹列表之前是空列表，现在group（）是专门装精灵的
        self.bullets=pygame.sprite.Group()
    def key_control(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:

            self.rect.top -= self.speed
        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:

            self.rect.bottom+= self.speed
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:

            self.rect.right += self.speed
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:

            self.rect.left -= self.speed
        if key_pressed[pygame.K_SPACE]:
            #发射子弹
            bullet=Bullet(self.screen,self.rect.left,self.rect.top,self.speed)
            self.bullets.add(bullet)

    def update(self):#调用keycontral和display时可直接调用该update方法
        self.key_control()
        self.display()

    def display(self):
        # 3将飞机图片贴到窗口
        self.screen.blit(self.player, self.rect)
        self.bullets.update()#调用group中的update（）
        self.bullets.draw(self.screen)#遍历所有子弹

class Enemyplane(pygame.sprite.Sprite):
    def __init__(self,screen):

        pygame.sprite.Sprite.__init__(self)  # 精灵类的初始化方法必用；
        self.player = pygame.image.load('./images/enemy1.png')
        self.rect = self.player.get_rect()  # 这里的rect指矩形，也就是通过图像间的矩形对象来判断是否碰撞
        self.rect.topleft = [0, 0]  # 飞机图片的左上角坐标
        self.screen = screen
        # 飞机速度
        self.speed = 10
        # 子弹列表之前是空列表，现在group（）是专门装精灵的
        self.bullets = pygame.sprite.Group()
        self.direction = 'right'
    def display(self):
        # 3将飞机图片贴到窗口
        self.screen.blit(self.player, self.rect)
        self.bullets.update()  # 调用group中的update（）
        self.bullets.draw(self.screen)  # 遍历所有子弹

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right+=self.speed-10
        elif self.direction == 'left':
            self.rect.right-=self.speed-10
        if self.rect.right>480-57:
            self.direction = 'left'
        elif self.rect.right<0:
            self.direction = 'right'
    def auto_fire(self):
        random_num=random.randint(1,10)
        if random_num == 8:
            bullet=EnemyBullet(self.screen,self.rect.left,self.rect.top,self.speed)
            self.bullets.add(bullet)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/bullet1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft=[ x+102/2-5/2,y-11]
        self.screen=screen
        self.speed=10
    def update(self):
        self.rect.top-=self.speed
        if self.rect.top<-11:#这里代码的意思是当子弹移出屏幕上方销毁子弹对象，否则子弹会一直存在消耗内存
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,speed):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/bullet2.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+56/2-5/2, y+43]
        self.screen=screen
        self.speed=10

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > 700:
            self.kill()


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./sound/game_music.ogg')
        pygame.mixer.music.set_volume(0.5)
    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)



def main():#整个程序控制
    sound=GameSound()
    sound.playBackgroundMusic()
    #1窗口
    screen=pygame.display.set_mode((480,700), 0, 32)
    #2图片背景
    background = pygame.image.load('./images/background.png')
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