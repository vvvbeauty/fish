import math
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import sys
import pygame
from pygame.locals import *
from libyuang import *

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

def wrap_angle(angle):
    return angle % 360

def hh(xT=200,yT=200,radiusX= 250,radiusY= 250):
    
    angle = 0.0
    pos = Point(0,0)
    old_pos = Point(0,0)
    print(dir(Point))
    posT=[]
    rangleT=[]
    while True:
        angle = wrap_angle(angle - 5)
        pos.x = math.sin( math.radians(angle) ) * radiusX
        pos.y = math.cos( math.radians(angle) ) * radiusY
        posT.append([pos.x+xT,pos.y+yT])
        delta_x = ( pos.x - old_pos.x )
        delta_y = ( pos.y - old_pos.y )
        rangle = math.atan2(delta_y, delta_x)
        if angle:
            rangled = wrap_angle( -math.degrees(rangle) )
        if not angle:
            rangled = wrap_angle( -math.degrees(rangle))+0
        rangleT.append(rangled)
        
        #rangleT.append(rangled)
        old_pos.x = pos.x
        old_pos.y = pos.y
        if angle==0:break
    rangleT[0]=rangleT[0]-90
    return posT,rangleT


def hu(angle1,angle2,r,cx,cy):
    i,count = 0,200
    PI = math.pi
    angle=0
    li=[]
    while i<5:
        angle = (angle1 * (count-i) + angle2 * (i)) / count
        x = cx+math.cos(angle) * r
        y = cy+math.sin(angle) * r
        i +=1
        li.append([x,y])
        #if i > count:i = 0
    return li

#def yuang(banjinX,banjinY,currX,currY,Ty=360,Xstep=5,er=2,Xv=0,Yv=0):
	#banjinX X轴半径和Y轴半径一样是椭圆
	#banjinY Y轴半径和X轴半径一样是圆
	#currX,currY显示偏移
	#Ty=360是圆

def main():
    img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,192,78,64]]
    img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
    axis1=angle1=li=axis2=angle2=[]
    
    axis1,angle1=yuang(300,400,500,500,660,10,2)
    axis2,angle2=hh(350,350,280,250)
    li=hu(50,180,300,400,400)
    #print(len(angle2),angle2[0],axis2[0])
    for i in range(len(angle2)):
        print(axis2[i],angle2[i] )
    
    screen = pygame.display.set_mode((1280,1280),0,(32,32))
    image2=pygame.image.load("me1.jpg")
    image2=pygame.transform.scale(image2,(1280,1280))
    image1 = pygame.image.load("fish2.png")
    img1x=[image1.subsurface(i) for i in img1]
    img2x=[image1.subsurface(i) for i in img2]
    clock = pygame.time.Clock()
    i,xx,tt=0,0,0
    while True:
        yu=pygame.transform.scale(img1x[i],(117,96))
        yu1=pygame.transform.rotate(yu,angle1[xx])
        yu2=pygame.transform.rotate(yu,angle2[tt])
        
        screen.blit(image2,(0,0))
        screen.blit(yu1,axis1[xx])
        screen.blit(yu2,axis2[tt])
        pygame.draw.aalines(screen,[255,0,0],True,axis1)
        pygame.draw.aalines(screen,[25,0,0],True,axis2)
        pygame.draw.aalines(screen,[255,0,0],True,li)
        
        
        pygame.display.update()
        clock.tick(60)
        xx+=1
        i+=1
        tt+=1
        if i==len(img1x):i=0
        if xx==len(angle1):xx=0
        if tt==len(angle2):tt=0
  
  
  
if __name__ == '__main__':
    
  
  
  
    main()