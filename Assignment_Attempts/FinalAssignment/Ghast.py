#
# Knight.py - setting up Knight Character
#

import pygame
from utilities import *

class Knight(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacleSprites):
        super().__init__(groups)
        # making png the Knight
        self.image = pygame.image.load('').convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)
        self.direciton = pygame.math.Vector2()
        self.speed = 5
        self.obstacleSprites = obstacleSprites

    def collision(self,direction):
        if direction == 'horizontal':
            for s in self.obstacleSprites:
                if s.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = s.rect.left
                    if self.direction.x < 0:
                        self.rect.left = s.rect.right

        if direction == 'vertical':
            for s in self.obstacleSprites:
                if s.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = s.rect.top
                    if self.direciton.y < 0:
                        self.rect.top = s.rect.bottom

        if self.rect.right, self.rect.left, self.rect.bottom, self.rect.top == False:
            self.direction.y + 1

        elif self.rect.top == True:
            if random.randint(1,3) == 1:
                self.direction.x = self.direction.x + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x -1
            else:
                self.direction.y = self.direction.y - 1
        elif self.rect.right == True:
            if random.randint(1,3) == 1:
                self.direction.y = self.direction.y + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x - 1
            else:
                self.direction.y = self.direction.y - 1
        elif self.rect.bottom == True:
            if random.randint(1,3) == 1:
                self.direction.x = self.direction.x + 1
            elif random.randint(1,3) == 2:
                self.direction.y = self.direction.y + 1
            else:
                self.direction.x = self.direction.x - 1
        elif self.rect.left == True:
            if random.randint(1,3) == 1:
                self.direction.y = self.direction.y + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x + 1
            else:
                self.direction.y = self.direction.y - 1

    def speedStabalise(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def update(self):
        self.collision()
        self.move(self.speed)

