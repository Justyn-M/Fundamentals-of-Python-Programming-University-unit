#
# knight.py - Setting up knight character
# 

import pygame
from utilities import *

class Knight(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacleSprites):
        super().__init__(groups)
        self.image = pygame.image.load('/home/justyn/FOP/FOPAssignment/graphics/run1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self. hitbox = self.rect.inflate(0,-26)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacleSprites = obstacleSprites

    def input(self):
        self.direction.y + 100

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

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

def update(self):
    self.input()
    self.move(self.speed)

