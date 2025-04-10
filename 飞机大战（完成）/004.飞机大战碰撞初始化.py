import random
import time
import pygame
from pygame.constants import *


#现在开始继承精灵类，精灵类可以实现碰撞检测，除此之外还有一些方便的功能，等待学习
class Heroplane(pygame.sprite.Sprite):
    bullets = pygame.sprite.Group()#存放玩家飞机所有子弹的组
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)#精灵类的初始化方法必用；
        self.player = pygame.image.load('images/me1.png')
        self.rect=self.player.get_rect()#这里的rect指矩形，也就是通过图像间的矩形对象来判断是否碰撞
        self.rect.topleft=[Manager.bg_size[0]/ 2 - 102 / 2,550]#飞机图片的左上角坐标
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
            Heroplane.bullets.add(bullet)

    def update(self):#调用keycontral和display时可直接调用该update方法
        self.key_control()
        self.display()

    def display(self):
        # 3将飞机图片贴到窗口
        self.screen.blit(self.player, self.rect)
        self.bullets.update()#调用group中的update（）
        self.bullets.draw(self.screen)#遍历所有子弹

    @classmethod
    def clear_bullets(cls):
        cls.bullets.empty()

class Enemyplane(pygame.sprite.Sprite):
    enemy_bullets=pygame.sprite.Group()
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)  # 精灵类的初始化方法必用；
        self.image = pygame.image.load('images/enemy1.png')
        self.rect = self.image.get_rect()  # 这里的rect指矩形，也就是通过图像间的矩形对象来判断是否碰撞

        x=random.randrange(1,Manager.bg_size[0],50)
        self.rect.topleft = [x, 0]  # 飞机图片的左上角坐标
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
        if self.rect.right > Manager.bg_size[0]-57:
            self.direction = 'left'
        elif self.rect.right < 0:
            self.direction = 'right'
        self.rect.bottom += self.speed-7
    def auto_fire(self):
        random_num=random.randint(1,40)
        if random_num == 8:
            bullet=EnemyBullet(self.screen,self.rect.left,self.rect.top,self.speed)
            self.bullets.add(bullet)
            Enemyplane.enemy_bullets.add(bullet)


    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()
    @classmethod
    def clear_bullets(cls):
        cls.enemy_bullets.empty()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/bullet1.png')
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
        self.image = pygame.image.load('images/bullet1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+56/2-5/2, y+43]
        self.screen=screen
        self.speed=10

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > Manager.bg_size[1]:
            self.kill()


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('sound/game_music.ogg')
        pygame.mixer.music.set_volume(0.5)
        self.me__bomb=pygame.mixer.Sound('sound/me_down.wav')

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)
    def playBombSound(self):
        pygame.mixer.Sound.play(self.me__bomb)
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
        if not self.mVisible:
            return
        self.screen.blit(self.mImage[self.mIndex],(self.mPos[0],self.mPos[1]))
        self.mIndex+=1
        if self.mIndex>=len(self.mImage):
            self.mIndex=0
            self.mVisible=False


class GameBackground(object):
    def __init__(self,screen):
        self.mImage1=pygame.image.load("images/background.png")
        self.mImage2 = pygame.image.load("images/background.png")
        self.screen=screen
        self.y1=0
        self.y2=-Manager.bg_size[1]
    def draw(self):
        self.screen.blit(self.mImage1,(0,self.y1))
        self.screen.blit(self.mImage1, (0, self.y2))
    def move(self):
        self.y1+=2
        self.y2+=2
        if self.y1>=Manager.bg_size[1]:
            self.y1=0
        if self.y2>=0:
            self.y2=-Manager.bg_size[1]
class Manager(object):#面向对象
    bg_size=(480,700)
    create_enemy_id=10
    game_over_id=11
    is_game_over=False
    over_time=3
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480,700), 0, 32)
        self.background=pygame.image.load('images/background.png')
        self.players=pygame.sprite.Group()  # 精灵组（pygame.sprite.Group）
                                            # 精灵组是一个容器，用于存储和管理多个精灵对象。它提供了以下功能：
                                            # 批量更新精灵状态：调用 update() 方法时，会自动调用组内每个精灵的 update() 方法。
                                            # 批量绘制精灵：调用 draw() 方法时，会自动将组内每个精灵绘制到屏幕上。
                                            # 精灵的添加和移除：可以动态地向组中添加或移除精灵。
        self.map=GameBackground(self.screen)
        self.enemies=pygame.sprite.Group()
        self.player_bomb=Bomb(self.screen,'player')#爆炸类里面的判断
        self.enemy_bomb=Bomb(self.screen,'enemy')
        self.sound=GameSound()

    def exit(self):
        print('退出')
        pygame.quit()
        exit()

    def show_over_text(self):
        self.drawText('gameover %d' %Manager.over_time,100,Manager.game_over_id/2,
                      textHeight=50,fontColor=[255,0,0])

    def game_over_text(self):
        self.show_over_text()
        Manager.over_time-=1
        if Manager.over_time==0:
            pygame.time.set_timer(Manager.game_over_id,0)
            Manager.over_time=3
            Manager.is_game_over=False
            self.start_game()

    def start_game(self):
        Enemyplane.clear_bullets()
        Heroplane.clear_bullets()
        manager=Manager()
        manager.main()
    def new_player(self):
        player=Heroplane(self.screen)
        self.players.add(player)


    def new_enemy(self):#创建敌机的对象添加到敌机组中
        enemy = Enemyplane(self.screen)
        self.enemies.add(enemy)

    def drawText(self,text,x,y,textHeight=30,fontColor=(255,0,0),backgroundColor=None):
        #通过字体文件获取字体对象
        font_obj=pygame.font.Font('images/shangshoutuhuati.ttf', textHeight)
        text_obj=font_obj.render(text,True,fontColor,backgroundColor)#True表示文字锯齿判断
        text_rect=text_obj.get_rect()
        text_rect.topleft=(x,y)
        self.screen.blit(text_obj,text_rect)


    def main(self):
        self.sound.playBackgroundMusic()
        self.new_player()
        pygame.time.set_timer(Manager.create_enemy_id,1000)
        self.new_enemy()
        while True:
            # 3将背景图片贴到窗口
            # self.screen.blit(self.background, (0, 0))
            self.map.move()
            self.map.draw()
            self.drawText('hp:100',0,0)
            if Manager.is_game_over:
                self.show_over_text()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                elif event.type == Manager.create_enemy_id:
                    self.new_enemy()
                elif event.type == Manager.game_over_id:
                    self.game_over_text()
            self.player_bomb.draw()
            self.enemy_bomb.draw()
            if self.players.sprites():
                isover=pygame.sprite.groupcollide(self.players,Enemyplane.enemy_bullets,False,True)#精灵间的碰撞
                if isover:
                    Manager.is_game_over=True
                    pygame.time.set_timer(Manager.game_over_id,1000)#开始游戏倒计时
                    print('中弹')
                    self.player_bomb.action(self.players.sprites()[0].rect)
                    self.players.empty()
                    self.sound.playBombSound()
            iscollide=pygame.sprite.groupcollide(self.players,self.enemies,True,True)#这是一个字典
            if iscollide:
                Manager.is_game_over=True
                pygame.time.set_timer(Manager.game_over_id,1000)
                items=list(iscollide.items())[0]#用items获取到列表中飞机
                print(items)
                x=items[0]
                y=items[1][0]
                self.player_bomb.action(x.rect)
                self.enemy_bomb.action(y.rect)
                self.sound.playBombSound()
            is_enemy=pygame.sprite.groupcollide(Heroplane.bullets,self.enemies,True,True)
            if is_enemy:
                items=list(is_enemy.items())[0]
                y=items[1][0]
                self.enemy_bomb.action(y.rect)
                self.sound.playBombSound()
            self.players.update()
            self.enemies.update()
            pygame.display.update()
            time.sleep(0.01)

if __name__ == '__main__':
    manager = Manager()
    manager.main()

