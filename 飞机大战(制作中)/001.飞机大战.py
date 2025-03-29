import pygame
import time
import pygame

pygame.init()
def main():#整个程序控制
    #1窗口
    screen=pygame.display.set_mode((480,700), 0, 32)
    #2图片背景
    background = pygame.image.load('./images/background.png')
    #2飞机图片
    player = pygame.image.load('./images/me1.png')


    x=480/2-102/2
    y=550

    #飞机速度
    speed=10
    while True:
        # 3将背景图片贴到窗口
        screen.blit(background, (0, 0))
        # 3将飞机图片贴到窗口
        screen.blit(player, (x, y))
        #获取事件
        for event in pygame.event.get():
            #判断事件类型
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # elif event.type == pygame.KEYDOWN:
            #     #检查按键是否是a或者LEFT
            #     if event.key == K_a or event.key==K_LEFT:
            #         print('左')
            #     # 检查按键是否是D或者RIGHT
            #     if event.key == K_d or event.key == K_RIGHT:
            #         print('右')
            #     elif event.key==K_SPACE:
            #         print('空格')
            key_pressed=pygame.key.get_pressed()
            if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
                print('上')
                y-=speed
            if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
                print('下')
                y+=speed
            if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
                print('右')
                x+=speed
            if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
                print('左')
                x-=speed
            if key_pressed[pygame.K_SPACE]:
                print('空格')

        #4show窗口内容
        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()





