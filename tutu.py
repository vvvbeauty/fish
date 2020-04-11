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
        self.imagex=self.rect.w
        self.imagey=self.rect.h
        self.center1=self.rect.center
        self.number=len(initial_position)
        #self.rect = self.image.fill(color, None, BLEND_ADD)
        #self.rect.topleft = initial_position

class MoveBall(Ball):
    def __init__(self, file1, initial_position, axis, angle,xy):
        super(MoveBall, self).__init__(file1, initial_position)
        self.count=0
        self.order1=0
        self.axis=axis
        self.angle=angle
        self.axis1 = self.axis[self.order1]
        self.angle1 = self.angle[self.order1]
        self.number1=len(angle)
        self.rotate=pygame.transform.rotate(self.image,self.angle1)
        self.xy=xy
        self.curx=self.xy[self.order1][0]+self.center1[0]
        self.cury=self.xy[self.order1][1]+self.center1[1]
        
        
 
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
        self.rotate=pygame.transform.rotate(self.image,self.angle1)
        self.curx=self.xy[self.order1][0]+self.center1[0]
        self.cury=self.xy[self.order1][1]+self.center1[1]
        

 
pygame.init()
screen = pygame.display.set_mode((1280,1280),0,(32,32))
sui= screen.get_rect()
image2=pygame.image.load("me1.jpg")
image2=pygame.transform.scale(image2,(sui.w,sui.h))
balls = []
img1=[[0,0,78,64],[0,64,78,64],[0,128,78,64],[0,128,78,64],[0,192,78,64]]
img2=[[0,256,78,64],[0,320,78,64],[0,384,78,64],[0,448,78,64]]
#axis1=angle1=axis2=angle2=[]

for t in range(18):
    j=random.randint(80,1200)
    axis3=[[i,j] for i in range(0,1200,random.randint(12,20))]
    angle3=[i*0 for i in range(len(axis3))]
    #balls.append(MoveBall("fish2.png",img1,axis3,angle3))
    
axis4=[[i,100] for i in range(0,1200,2)]
angle4=[i*0 for i in range(len(axis4))]
#del j
random.randint(0,0)
del t
for yy in range(5,16):
    gh=random.randint(8,10)
    axis5,angle5,xy5=yuang(10+yy*30,10+yy*30,600,600,660,gh,2)
    
    for j in range(5,30,5):
        axis7=[axis5[i] for i in range(j,len(axis5))]
        for i in range(j):
            axis7.append(axis5[i])
        angle7,xy7=jiaodu(axis7)
        #balls.append(MoveBall("fish2.png",img1,axis7,angle7))
    
    axis6=[i for i in axis5[::-1]]
    #angle6=[i for i in angle5[::-1]]
    angle6,xy6=jiaodu(axis6)
    
    #balls.append(MoveBall("fish2.png",img1,axis5,angle5))
    #balls.append(MoveBall("fish2.png",img1,axis6,angle6))
    
#del gh   
axis2,angle2,xy2=yuang(200,400,500,500,660,10,2)
def beisaier():
    #贝塞尔曲线
    #xs = [0,20,50,100,150,180,200,150,100,30,0,-50]
    #ys = [0,80,100,100,150,160,250,300,400,500,700,800]
    xs=[]
    ys=[]
    y=random.randint(0,1200)
    xs.append(0)
    ys.append(y)
    for i in range(2):
        x=random.randint(0,1200)
        y=random.randint(0,1200)
        xs.append(x)
        ys.append(y)
    xs.append(1278)
    ys.append(y)
    num = len(xs)*15
    b_xs = []
    b_ys = []
    bezier_curve(xs,ys,num,b_xs,b_ys)
    axis88=[[b_xs[i],b_ys[i]] for i in range(len(b_xs))]
    angle88,xy88=jiaodu(axis88,0)
    #print(angle88)
    balls.append(MoveBall("fish2.png",img1,axis88,angle88,xy88))
    
    x=random.randint(18,33)
    for j in range(6,x,6):
        t=j
        axis7=[axis88[ic] for ic in range(j,len(axis88))]
        for i in range(t):
            axis7.append(axis88[i])
        angle7,xy7=jiaodu(axis7,0)
        balls.append(MoveBall("fish2.png",img1,axis7,angle7,xy7))
#贝塞尔曲线
    
    
    


#balls.append(MoveBall("fish2.png",img1,axis2,angle2))

#balls.append(MoveBall("fish2.png",img1,axis3,angle3))
#balls.append(MoveBall("fish2.png",img1,axis4,angle4))
#balls.append(MoveBall("fish2.png",img2,axis2,angle2))
beisaier()
beisaier()
myfont = pygame.font.SysFont("DejaVuSans", 64)


sco=0
label=0
#label1= myfont.render("score:{}".format(sco), 1, (255, 255, 255))
while True:
    if pygame.event.poll().type == QUIT: break
    
 
    #screen.fill((0,0,0,))
    #current_time = pygame.time.get_ticks()
    
            

    screen.blit(image2,[0,0])
    for b in balls:
        b.update()
        screen.blit(b.rotate,b.axis1)
        #pygame.draw.aalines(screen,[0,255,0],False,b.axis)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
               
               label = myfont.render('{0}'.format(event.pos), 1, (255, 255, 255))
               for b in balls:
                   b.update()
                   x=abs(int(event.pos[0]-b.curx))
                   y=abs(int(event.pos[1]-b.cury))
                   if x<b.imagex/2 and y<b.imagey/2:
                       sco+=1
                       balls.remove(b)
                       
                   
    label1= myfont.render("score:{}".format(sco), 1, (255, 255, 255))                
    
    screen.blit(label1,(0,0))
    if label:
        screen.blit(label, (420, 0))
        
    pygame.display.update()
    pygame.time.delay(100)
    

            
