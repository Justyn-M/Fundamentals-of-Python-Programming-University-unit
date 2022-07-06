#
# character.py - setting up characters
#

import pygame
from mapSetup import *
from entities import Entity

class Knight(Entity):
    def __init__(self, pos, groups, obstacleSprites):
        super().__init__(groups)
        self.image = pygame.image.load('/home/justyn/FOP/Assignment/graphics/run1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.speed = 5

        self.obstacleSprites = obstacleSprites

    def input(self):

        right_collision_detector =


        if self.front_collision_detector,self.right_collision_detector,self.left_collision_detector,self.back_collision_detector == False:
            self.direction.y + 1
        elif self.front_colision_detector == True:
            if random.randint(1,3) == 1:
                self.direction.x = self.direction.x + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x -1
            else:
                self.direction.y = self.direction.y - 1
        elif self.right_collision_detector == True:
            if random.randint(1,3) == 1:
                self.direction.y = self.direction.y + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x - 1
            else:
                self.direction.y = self.direction.y - 1
        elif self.back_collision_detector == True:
            if random.randint(1,3) == 1:
                self.direction.x = self.direction.x + 1
            elif random.randint(1,3) == 2:
                self.direction.y = self.direction.y + 1
            else:
                self.direction.x = self.direction.x - 1
        elif self.left_collision_detector == True:
            if random.randint(1,3) == 1:
                self.direction.y = self.direction.y + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x + 1
            else:
                self.direction.y = self.direction.y - 1


    def movement(self,speed):
        if self.direction.magnitude() != 0:
            #magnitude is length of vector, makes it so speed is same in all directions. 
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

   def update(self):
       self.input()
       self.move(self.speed)


         
