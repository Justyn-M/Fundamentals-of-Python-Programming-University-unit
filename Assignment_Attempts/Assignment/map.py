 map.py - file to call sprites into map
# 

import pygame
from mapSetup import *
from objects import Object
from character import Knight
from debugger import debugger
from csvlayouts import *
from mobs import Mob

class Map:
    def __init__(self):

        # sprite groups
        self.visableSprites = YsortCameraGroup()
        self.obstacleSprites = pygame.sprite.Group()
        # code to  display surface
        self.surfaceDisplay = pygame.display.get_surface()

        self.setMap()

    def setMap(self):
        layouts = {
            'boundary': import_csv_layout('/home/justyn/FOP/Assignment/csv_files/map_Barriers.csv'),
            'entities': import_csv_layout('/home/justyn/FOP/Assignment/csv_files/Entities.csv')
        }
        ## RI = row index, CI = Column index
        for style,layout in layouts.items():
            for RI,row in enumerate(layout):
                for CI, col in enumerate(row):
                    if col != '-1':
                        x = CI * Tilesize
                        y = RI * Tilesize
                        if style == 'boundary':
                            Object((x,y),[self.obstacleSprites], 'invisible')
                        if style == 'entities':
                            if col == '34' and '35':
                                Mob('archer',(x,y),[self.visibleSprites,self.obstacleSprites])


              self.character = Knight((700,1500),[self.visableSprites],self.obstacleSprites)
    def run(self):
        self.visableSprites.customDraw(self.character)
        self.visableSprites.update()
        #debugger(self.player.direction)

class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        # general setup
        super().__init__()
        self.surfaceDisplay = pygame.display.get_surface()
        self.halfWidth = self.surfaceDisplay.get_size()[0] // 2
        self.halfHeight = self.surfaceDisplay.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating 1st layer as floor
        self.floorSurface = pygame.image.load('/home/justyn/FOP/Assignment/graphics/floor.png').convert()
        self.floor_rect = self.floorSurface.get_rect(topleft = (0,0))

    def customDraw(self,character):
        self.offset.x = character.rect.centerx - self.halfWidth
        self.offset.y = character.rect.centery - self.halfHeight

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.surfaceDisplay.blit(self.floorSurface,floor_offset_pos)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.surfaceDisplay.blit(sprite.image,offset_pos)
