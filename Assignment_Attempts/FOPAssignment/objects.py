#
# objects.py - setting up objects
# 

import pygame
from utilities import *

class Object(pygame.sprite.Sprite):
    def __init__(self,pos,groups,spriteType,surface = pygame.Surface((Tile_Area,Tile_Area))):
        super().__init__(groups)
        self.spriteType = spriteType
        self.image = surface
        if spriteType == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - Tile_Area))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) 
