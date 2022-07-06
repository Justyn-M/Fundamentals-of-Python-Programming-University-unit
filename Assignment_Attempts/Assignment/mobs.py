import pygame
from mapSetup import *
from entity import Entity

class Mob(Entity):
    def __init__(self,mobName,pos,groups,obstableSprites):
        
        # setup
        super().__init__(groups)
        self.spriteType = 'mob'

        # graphics
        self.importGraphics(mobName)
        self.status = 'run'
        self.image =  self.animations[self.status][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)

    def movement.

    def importGraphics(self):
        self.animations = {'run':[],'attack':[]]}
        mainPath = f'/home/FOP/Assignment/archer/archer/{name}/'
        for animation in self.animations.keys():
            self.animation[animation] = import_folder(mainPath + animation)

