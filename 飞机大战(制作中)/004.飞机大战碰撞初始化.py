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
        self.image = pygame.image.load('./images/enemy1.png')
        self.rect = self.image.get_rect()  # 这里的rect指矩形，也就是通过图像间的矩形对象来判断是否碰撞
        self.rect.topleft = [0, 0]  # 飞机图片的左上角坐标

        # 飞机速度
        self.speed = 10
        self.screen = screen
        # 子弹列表之前是空列表，现在group（）是专门装精灵的
        self.bullets = pygame.sprite.Group()
        self.direction = 'right'
    def display(self):
        # 3将飞机图片贴到窗口
        self.screen.blit(self.image, self.rect)
        self.bullets.update()  # 调用group中的update（）
        self.bullets.draw(self.screen)  # 遍历所有子弹

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed-4
        elif self.direction == 'left':
            self.rect.right -= self.speed-4
        if self.rect.right > 480-57:
            self.direction = 'left'
        elif self.rect.right < 0:
            self.direction = 'right'
    def auto_fire(self):
        random_num=random.randint(1,20)
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

class Bomb(object):
    def __init__(self,screen,type):
        self.screen = screen
        if type=='enemy':
            self.mImage=[pygame.image.load
                         ("./images/enemy1_down"+str(v)+".png")for v in range(1,4) ]#用拼接的方式加上列表推导式将几个图片连续地传入实现视觉上的动态展示
        else:
            self.mImage=[pygame.image.load
                         ("./images/me_destroy_"+str(v)+".png")for v in range(1,4) ]
        self.mIndex=0#爆炸图片循环的索引
        self.mPos=[0,0]#爆炸的坐标
        self.mVisible=False
    def action(self,rect):
        #触发爆炸的方法draw
        self.mPos[0]=rect.left#爆炸坐标
        self.mPos[1]=rect.top
        self.mVisible=True#打开爆炸的开关

    def draw(self):
        while self.mVisible:
            for image in self.mImage:
                self.screen.blit(image, self.mPos)

        pygame.display.flip()
        self.mVisible = False

class Manager(object):#面向对象
    def __init__(self):
        self.screen = pygame.display.set_mode((480,700), 0, 32)
        self.background=pygame.image.load('./images/background.png')
        self.players=pygame.sprite.Group()  # 精灵组（pygame.sprite.Group）
                                            # 精灵组是一个容器，用于存储和管理多个精灵对象。它提供了以下功能：
                                            # 批量更新精灵状态：调用 update() 方法时，会自动调用组内每个精灵的 update() 方法。
                                            # 批量绘制精灵：调用 draw() 方法时，会自动将组内每个精灵绘制到屏幕上。
                                            # 精灵的添加和移除：可以动态地向组中添加或移除精灵。
        self.enemies=pygame.sprite.Group()
        self.player_bomb=Bomb(self.screen,'player')#爆炸类里面的判断
        self.enemy_bomb=Bomb(self.screen,'enemy')
        self.sound=GameSound()

    def exit(self):
        print('退出')
        pygame.quit()
        exit()
    def new_enemy(self):#创建敌机的对象添加到敌机组中
        enemy = Enemyplane(self.screen)
        self.enemies.add(enemy)
    def new_player(self):
        player=Heroplane(self.screen)
        self.players.add(player)
    def main(self):
        self.sound.playBackgroundMusic()
        self.new_player()
        self.new_enemy()
        while True:
            # 3将背景图片贴到窗口
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()

            self.player_bomb.draw()
            self.enemy_bomb.draw()
            iscollide=pygame.sprite.groupcollide(self.players,self.enemies,True,True)#这是一个字典
            if iscollide:
                items=list(iscollide.keys())[0]#用items获取到列表中飞机
                print(items)
                x=items[0]
                y=items[1][0]
                self.player_bomb.action(x.rect)
                self.enemy_bomb.action(y.rect)
            self.players.update()
            self.enemies.update()
            pygame.display.update()
            time.sleep(0.01)

if __name__ == '__main__':
    manager = Manager()
    manager.main()

