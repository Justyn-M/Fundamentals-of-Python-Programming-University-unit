#
# Knight.py - setting up Knight Character
#

import pygame
from utilities import *

class Knight(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacleSprites):
        super().__init__(groups)
        # making png the Knight
        self.image = pygame.image.load('/home/justyn/FOP/FinalAssignment/graphics/Barrel Knight/Barrel Knight/run/run1.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)
        self.direciton = pygame.math.Vector2()
        self.speed = 5
        self.obstacleSprites = obstacleSprites
        self.captured = False

    def move(self):
        if self.rect.right == False and  self.rect.left == False and self.rect.bottom == False and self.rect.top == False:
            self.direction.y + 1

        elif self.rect.top == True and self.captured == False:
            if random.randint(1,3) == 1:
                self.direction.x = self.direction.x + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x -1
            else:
                self.direction.y = self.direction.y - 1
        elif self.rect.right == True and self.captured == False:
            if random.randint(1,3) == 1:
                self.direction.y = self.direction.y + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x - 1
            else:
                self.direction.y = self.direction.y - 1
        elif self.rect.bottom == True and self.captured == False:
            if random.randint(1,3) == 1:
                self.direction.x = self.direction.x + 1
            elif random.randint(1,3) == 2:
                self.direction.y = self.direction.y + 1
            else:
                self.direction.x = self.direction.x - 1
        elif self.rect.left == True and self.captured == False:
            if random.randint(1,3) == 1:
                self.direction.y = self.direction.y + 1
            elif random.randint(1,3) == 2:
                self.direction.x = self.direction.x + 1
            else:
                self.direction.y = self.direction.y - 1
        # elif self.capture == True:
           #pygame.quit()
           #sys.exit)


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

    def speedStabalise(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def update(self):
        self.move()
        self.speedStabalise(self.speed)

