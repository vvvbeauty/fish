import pygame
from pygame.locals import *
 
class Ball(pygame.sprite.Sprite):
    def __init__(self, file1,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.order=0
        self.images1 = pygame.image.load(file1)
        self.images=[self.images1.subsurface(i) for i in initial_position]
        self.image=self.images[self.order]
        self.number=len(initial_position)
        #self.rect = self.image.fill(color, None, BLEND_ADD)
        #self.rect.topleft = initial_position

class MoveBall(Ball):
    def __init__(self, file1, initial_position, axis, angle):
        super(MoveBall, self).__init__(file1, initial_position)
        self.order1=0
        self.axis=axis
        self.angle=angle
        self.axis1 = self.axis[self.order1]
        self.angle1 = self.angle[self.order1]
        self.number1=len(angle)
        
 
    def update(self):
        if self.order >=self.number-1:
            self.order=-1
        self.order+=1
        self.image=self.images[self.order]
        if self.order1 >=self.number1-1:
            self.order1=-1
        self.order1+=1
        self.axis1 = self.axis[self.order1]
        self.angle1 = self.angle[self.order1]

 
pygame.init()
screen = pygame.display.set_mode([350, 350])
image2=pygame.image.load("me1.jpg")
balls = []
img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,128,78,64],[0,192,78,64]]
img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
axis1=[[i,50] for i in range(0,230,3)]
angle1=[i*0 for i in range(len(axis1))]
axis2=[[i,100] for i in range(0,245,1)]
angle2=[i*0 for i in range(len(axis2))]
balls.append(MoveBall("fish2.png",img1,axis1,angle1))
balls.append(MoveBall("fish2.png",img2,axis2,angle2))

while True:
    if pygame.event.poll().type == QUIT: break
 
    #screen.fill((0,0,0,))
    #current_time = pygame.time.get_ticks()
    screen.blit(image2,[0,0])
    for b in balls:
        b.update()
        i=pygame.transform.rotate(b.image,b.angle1)
        screen.blit(i,b.axis1)
    pygame.display.update()
    pygame.time.delay(10)

            
