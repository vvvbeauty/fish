# -*- coding:utf-8 -*-
import pygame_sdl2 as pygame
import time

#MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]




def load_image(file, width=None,height=None, number=None):
    #file = os.path.join(MAIN_DIR, '', file)
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if width == None:
        return surface
    #height = surface.get_height()
 
    return [surface.subsurface(
        Rect((0,i * width), (height,width))
        ) for i in range(number)]
 
class SunFlower(pygame.sprite.Sprite):
    _width = 110
    _height = 240
    _number = 9
    images = []
    def __init__(self):
        self.order = 0
        pygame.sprite.Sprite.__init__(self)
        if len(self.images) == 0:
            self.images = load_image("actor_fish_dayu_hv.png", self._width, self._height,self._number)
        self.image = self.images[self.order]
        self.rect = Rect(0, 0, self._height, self._width)
 
    def update(self):
        if self.order >= self._number - 1:
            self.order = -1
        self.order += 1
        self.image = self.images[self.order]



pygame.sprite.Sprite.__init__(SunFlower())
screen = pygame.display.set_mode((900, 400))
t=SunFlower()
while True:
    screen.blit(t.image,(100,100))
    t.update()
    pygame.display.update()

#img1=[[0,i*110,240,110] for i in range(9)]
#print(len(img1))