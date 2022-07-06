#
# objects.py - setting up objects
#

import pygame
from mapSetup import *

class Object(pygame.sprite.Sprite):
    def __init__(self,pos,groups,spriteType,surface = pygame.Surface((Tilesize,Tilesize))):
        super().__init__(groups)
        self.spriteType = spriteType
        self.image = surface
        if spriteType == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - Tilesize))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
