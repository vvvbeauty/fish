#!/usr/bin/env python
import numpy as np
#import matplotlib.pyplot as plt
import pygame_sdl2 as pygame
 
def one_bezier_curve(a,b,t):
    return (1-t)*a + t*b
 
#xs表示原始数据
#n表示阶数
#k表示索引
def n_bezier_curve(xs,n,k,t):
    if n == 1:
        return one_bezier_curve(xs[k],xs[k+1],t)
    else:
        return (1-t)*n_bezier_curve(xs,n-1,k,t) + t*n_bezier_curve(xs,n-1,k+1,t)
 
def bezier_curve(xs,ys,num,b_xs,b_ys):
    n = len(xs) - 1
    t_step = 1.0 / (num - 1)
    t = np.arange(0.0,1+t_step,t_step)
    for each in t:
        b_xs.append(n_bezier_curve(xs,n,0,each))
        b_ys.append(n_bezier_curve(ys,n,0,each))
 
def main():
    
    #贝塞尔曲线
    xs = [0,20,50,100,150,180,200,150,100,30]
    ys = [0,80,100,100,150,160,250,300,400,500]
    num = 100
    b_xs = []
    b_ys = []
    bezier_curve(xs,ys,num,b_xs,b_ys)
    #贝塞尔曲线
    
    
    yy1=[[b_xs[i],b_ys[i]] for i in range(len(b_xs))]
    print(type(yy1),len(yy1))
    yy2=list(zip(xs,ys))
    #print(yy2)
    screen = pygame.display.set_mode((640,960),0,32)
    while True:
        
        image2=pygame.image.loady("me1.jpg")
        screen.blit(image2,[0,0])
        pygame.draw.aalines(screen,[0,255,0],False,yy1)
        pygame.draw.aalines(screen,[0,255,0],False,yy2)
        pygame.display.update()
        pygame.time.delay(1000)
    #print(yy1)
    #print(yy2)
    #plt.figure()
    #plt.ploty(b_xs,b_ys)
    #plt.plot(xs,ys)
    #plt.show()
 
if __name__ == "__main__":
    main()
 