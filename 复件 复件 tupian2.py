# -*- coding:utf-8 -*-
import pygame
import time

def main():
  #1. 创建窗口
  screen = pygame.display.set_mode((640,960),0,32)
  #screen.fill([255,255,255])
  #2. 创建一个背景图片
  img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,128,78,64],[0,192,78,64]]
  img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
  img1x=[[10,1],[20,3],[30,8],[40,15],[50,30],[60,40],[50,50],[50,60]]
  img2_1=[[0,0],[20,60],[30,60],[40,60],[50,60],[60,60],[70,60],[80,60],[70,110]]
  img1r=[0,-10.2,-30,-50,-60,-65,-70,-75]

  img1yuan=[[303,101],[325,103],[351,107],[373,114],[394,127],[414,136],[438,157],[453, 172],[466, 191],[479, 211],[490, 238],[494, 252],[497, 282],[498, 312],[498, 329],[495, 346],[486, 370],[476, 396],[462, 414],[447, 432],[426, 455],[405, 471],[387, 480],[349, 493],[313, 498],[295, 498],[265, 496],[244, 491],[222, 482],[201, 472],[186, 463],[168, 447],[149, 432],[140, 418],[122, 393],[111, 367],[104, 339],[99, 311],[100, 284],[105, 249],[112, 226],[124, 208],[131, 194],[142, 175],[170, 149],[185, 136],[204, 124],[223, 120],[248, 110],[278, 101]]
  img1yuanjiao=[-7.2,-14.4, -21.6, -28.8, -36.0, -43.2, -50.4, -57.6, -64.8, -72.0, -79.2, -86.4, -93.6, -100.8, -108.0, -115.2, -122.4, -129.6, -136.8, -144.0, -151.2, -158.4, -165.6, -172.8, -180.0, -187.2, -194.4, -201.6, -208.8, -216.0, -223.2, -230.4, -237.6, -244.8, -252.0, -259.2, -266.4, -273.6, -280.8, -288.0, -295.2, -302.4, -309.6, -316.8, -324.0, -331.2, -338.4, -345.6, -352.8, -360.0,0]
  image1 = pygame.image.load("fish2.png")
  image2=pygame.image.load("me1.jpg")
  image2=pygame.transform.rotate(image2,1)
  image2=pygame.transform.scale2x(image2)
  screen.blit(image2,(0,0))
  pygame.display.update()
  #print(dir(pygame.display.set_mode()))
  #print(help(pygame.display))
  i=0
  j=0
  x=0
  y=0
  t=0
  xx=0
  tt=1
  screenx=pygame.display.get_surface()
  screeny1=screenx.subsurface(0,0,78,64)
  print(dir(pygame.draw.circle))
  while True:
    
    background=image1.subsurface(img1[i])
    background2=pygame.transform.scale(background,(117,96))
    background=pygame.transform.rotate(background2,img1r[xx])
    yuan=pygame.transform.rotate(background2,img1yuanjiao[j])
    background1=image1.subsurface(img2[i])
    
    #screen.fill([0,0,0])
    #screen.blit(image2,(0,0))
    screen.blit(background1, (0,0))
    screen.blit(background, img1x[xx])
    screen.blit(background2, img2_1[xx])
    pygame.draw.circle(screen,[0,255,0],[350,350],210,1)
    screen.blit(yuan,img1yuan[j])
    
    pygame.display.update()
    time.sleep(0.5)
    
    #print(i,t,tt,xx)
    #screen.blit(screeny1,(0,y))
    #pygame.display.flip()
    if tt==1:xx+=1
    if tt==0:xx-=1
    i+=1
    j+=1
    if j==50:
      j=0
    #t+=1
    if xx==7:
        tt=0
    if xx==0:
        tt=1
    if i==4:
        i=0
    #if t%5==0:
    #if t%10==0:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        exit(0)
      elif event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1:
          print(event.pos)
      




if __name__ == "__main__":
  main()
