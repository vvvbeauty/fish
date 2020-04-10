import pygame,random
from pygame.locals import *
from libyuang import *
 
class Ball(pygame.sprite.Sprite):
    def __init__(self, file1,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.order=0
        self.images1 = pygame.image.load(file1)
        self.images=[self.images1.subsurface(i) for i in initial_position]
        self.image=self.images[self.order]
        self.rect=self.image.get_rect()
        self.number=len(initial_position)
        #self.rect = self.image.fill(color, None, BLEND_ADD)
        #self.rect.topleft = initial_position

class MoveBall(Ball):
    def __init__(self, file1, initial_position, axis, angle):
        super(MoveBall, self).__init__(file1, initial_position)
        self.count=0
        self.order1=0
        self.axis=axis
        self.angle=angle
        self.axis1 = self.axis[self.order1]
        self.angle1 = self.angle[self.order1]
        self.number1=len(angle)
        
 
    def update(self):
        self.count+=1
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
screen = pygame.display.set_mode((1280,1280),0,(32,32))
image2=pygame.image.load("me1.jpg")
image2=pygame.transform.scale(image2,(1280,1280))
balls = []
img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,128,78,64],[0,192,78,64]]
img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
#axis1=angle1=axis2=angle2=[]

for t in range(18):
    j=random.randint(80,1200)
    axis3=[[i,j] for i in range(0,1200,random.randint(12,20))]
    angle3=[i*0 for i in range(len(axis3))]
    balls.append(MoveBall("fish2.png",img1,axis3,angle3))
    
axis4=[[i,100] for i in range(0,1200,2)]
angle4=[i*0 for i in range(len(axis4))]
#del j
random.randint(0,0)
del t
for yy in range(5,16):
    gh=random.randint(300,500)
    axis5,angle5=yuang(10+yy*30,10+yy*30,600,600,660,8,2)
    
    for j in range(5,30,5):
        axis7=[axis5[i] for i in range(j,len(axis5))]
        for i in range(j):
            axis7.append(axis5[i])
        angle7=jiaodu(axis7)
        balls.append(MoveBall("fish2.png",img1,axis7,angle7))
    #angle6=[i for i in angle5[::-1]]
    axis6=[i for i in axis5[::-1]]
    angle6=jiaodu(axis6)
    
    #balls.append(MoveBall("fish2.png",img1,axis5,angle5))
    balls.append(MoveBall("fish2.png",img1,axis6,angle6))
    
#del gh   
axis2,angle2=yuang(200,400,500,500,660,10,2)

#贝塞尔曲线
xs = [0,20,50,100,150,180,200,150,100,30,0,-50]
ys = [0,80,100,100,150,160,250,300,400,500,700,800]
num = 100
b_xs = []
b_ys = []
bezier_curve(xs,ys,num,b_xs,b_ys)
axis88=[[b_xs[i],b_ys[i]] for i in range(len(b_xs))]
angle88=jiaodu(axis88,0)
balls.append(MoveBall("fish2.png",img1,axis88,angle88))
#贝塞尔曲线
    
    
    


balls.append(MoveBall("fish2.png",img1,axis2,angle2))

balls.append(MoveBall("fish2.png",img1,axis3,angle3))
balls.append(MoveBall("fish2.png",img1,axis4,angle4))
#balls.append(MoveBall("fish2.png",img2,axis2,angle2))

while True:
    if pygame.event.poll().type == QUIT: break
 
    #screen.fill((0,0,0,))
    #current_time = pygame.time.get_ticks()
    screen.blit(image2,[0,0])
    for b in balls:
        b.update()
        #if b.count%50==0:
            #b.order1=0
        i=pygame.transform.rotate(b.image,b.angle1)
        screen.blit(i,b.axis1)
    pygame.display.update()
    pygame.time.delay(10)

            
