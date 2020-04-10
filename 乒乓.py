# -*- coding:utf-8 -*-
import pygame_sdl2 as pygame
import time,math,random

def main():
  #1. 创建窗口
  screen = pygame.display.set_mode((640,960),0,32)
  #screen.fill([255,255,255])
  #2. 创建一个背景图片
  img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,192,78,64]]
  img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
  #img1x=[[10,1],[20,3],[30,8],[40,15],[50,30],[60,40],[70,50],[70,50]]
  
  img1r=[-17.18873414713289, ]
  
  img2x=[[10,1],[20,4],[30,7],[40,10],[50,13],
  [60,16],[70,19],[80,22],[90,25],[100,28],
  [110,31]]

  tx1=10
  ty1=1
  i=0
  while tx1<=640:
  	#print('['+str(tx1)+','+str(ty1)+'],',end='\r'),
  	tx1+=10
  	ty1+=3
  	#img2x[i][0]=tx1
  	#img2x[i][1]=ty1
  	i+=1
  print(i,'\n')
  i=0
  for yy in range(len(img2x)-1):
  	yy1=img2x[yy+1][0]-img2x[yy][0]
  	yy2=img2x[yy+1][1]-img2x[yy][1]
  	yy3=math.atan2(yy2,yy1)
  	yy4=math.tan(yy3)*-180/3.1415926
  	#print(yy,yy2,yy1,yy3,yy4)
  	#print(str(yy4)+r','),
  	#img1r[i]=yy4
  	i+=1

  image1 = pygame.image.load("fish2.png")
  image2=pygame.image.load("me1.jpg")
  image2=pygame.transform.rotate(image2,90)
  image2=pygame.transform.scale(image2,(960,1260))
  screen.blit(image2,(0,0))
  pygame.display.update()
  #print(dir(pygame.display.set_mode()))
  #print(help(pygame.display))
  i=0
  j=0
  
  y=54
  t=0

  tt=1
  ttt=0
  ttt1=0
  screenx=pygame.display.get_surface()
  screeny1=screenx.subsurface(10,10,115,44)
  while True:
    background=image1.subsurface(img1[i])
    background2=pygame.transform.scale(background,(117,96))
    #background=pygame.transform.rotate(background,img1r[xx])
    background=pygame.transform.rotate(background2,-17.18873414713289)
    
    background1=image1.subsurface(img2[j])
    background1=pygame.transform.scale(background1,(117,96))
    
    #screen.fill([0,0,0])
    screen.blit(image2,(0,0))
    
    screen.blit(background1, (0,0))
    screen.blit(screeny1,(0,y));
    #screen.blit(background, img2x[xx])
    screen.blit(background, img2x[0])
    screen.blit(background, img2x[10])
    screen.blit(background2,img2x[1])
    screen.blit(background2,img2x[2])
    pygame.draw.lines(screen,[255,0,0],True,img1yuan,2)
    print(img2x[0])
    pygame.display.update()
    time.sleep(0.1)
    
    #screen.blit(screeny1,(0,y))
    #pygame.display.flip()
    t+=1
    ttt+=1
    ttt1+=1
    i+=1
    y+=1
    img2x[0][0]+=10
    img2x[0][1]+=3
    img2x[10][0]+=10
    img2x[10][1]+=3
    img2x[1][0]+=5
    img2x[2][0]+=5
    if i==4:
    	i=0
    if j==3:
    	j=0
    if t%10==0:
    	 j+=1
    if y==640:
    	y=0
    if ttt==85:
    	ttt=0
    	img2x[0][0]=10
    	img2x[0][1]=random.randint(10,960)
    	img2x[10][0]=12
    	img2x[10][1]=random.randint(50,960)
    if ttt1==170:
    	ttt1=0
    	img2x[1][1]=random.randint(50,960)
    	img2x[1][0]=10
    	img2x[2][1]=random.randint(50,960)
    	img2x[2][0]=15
  
    
      




if __name__ == "__main__":
  main()
