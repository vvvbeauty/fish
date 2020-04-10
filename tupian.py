# -*- coding:utf-8 -*-
import pygame
import time

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((370,598),0,32)
    screen.fill([255,255,255])
    #2. 创建一个背景图片

    #img=[0,0,78,64][0,64,78,64][0,128,78,64][0,128,78,64][0,192,78,64][0,256,78,64][0,320,78,64][0,384,78,64][0,448,78,64]
    
    image1 = pygame.image.load("fish2.png").convert_alpha()
    #print(dir(pygame.display.set_mode()))
    #print(help(pygame.display.set_mode().copy))
    i=0
    while True:
        background=image1.subsurface(0,i,78,64)
        screen.blit(background, (0,0))
        
        pygame.display.update()
        time.sleep(1)
        #pygame.display.flip()
        i+=64
        if i==512:
            i=0




if __name__ == "__main__":
    main()
