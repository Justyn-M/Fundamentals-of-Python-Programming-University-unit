#
# map.py - file to call sprites into map
#

import pygame
from utilities import *
from objects import Object
from Knights import Knight
from csvlayouts import *
from random import choice

class Map:
    def __init__(self):
    # code defines types of sprites and creates the map surface

        # Sprite groups
        self.visibleSprites = Camera()

        self.obstacleSprites = pygame.sprite.Group()
        # code to display surface
        self.surfaceDisplay = pygame.display.get_surface()
        # Displaying map
        self.setMap()

    def setMap(self):
        layers = {
                'boundary': import_csv_layout('/home/justyn/FOP/FinalAssignment/map_Barriers.csv')
                }
        ## RI = Row Index, CI = Column Index
        for style,layer in layers.items():
            for RI,row in enumerate(layer):
                for CI, col in enumerate(row):
                    if col != '-1':
                        x = CI * Tile_Area
                        y = RI * Tile_Area
                        if style == 'boundary':
                            Object((x,y),[self.obstacleSprites], 'invisible')

        self.Knights = Knight((700,1500),[self.visibleSprites],self.obstacleSprites)

    def run(self):
        self.visibleSprites.customDraw(self.Knights)
        self.visibleSprites.update()

class Camera(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.surfaceDisplay = pygame.display.get_surface()
        self.halfWidth = self.surfaceDisplay.get_size()[0] // 2
        self.halfHeight = self.surfaceDisplay.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating 1st layer as floor
        self.floorSurface = pygame.image.load('/home/justyn/FOP/FinalAssignment/graphics/floor.png').convert()
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

