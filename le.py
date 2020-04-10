# -*- coding:utf-8 -*-
import pygame_sdl2 as pygame
import time
from pygame.locals import *

#MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]




def load_image(file,height=None, width=None, number=None):
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
    _width = 64
    _height = 78
    _number = 9
    images = []
    def __init__(self):
        self.order = 0
        #pygame.sprite.Sprite.__init__(self)
        if len(self.images) == 0:
            self.images = load_image("fish2.png", self._height, self._width,self._number)
        self.image = self.images[self.order]
        self.rect = Rect(0, 0, self._width, self._height)
 
    def update(self):
        if self.order >= self._number - 1:
            self.order = -1
        self.order += 1
        self.image = self.images[self.order]



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 400))
    app=SunFlower()
    print(dir(app))
    d=app.update.im_self
    while True:
        screen.blit(d.image,(100,100))
        pygame.display.updated()
        app.update()
        pygame.time.delay(1000)


#img1=[[0,i*110,240,110] for i in range(9)]
#print(len(img1))