#
# simScreen.py - file that runs sim screen
#

import pygame, sys
from mapSetup import *
from map import Map

class Sim:
    def __init__(self):
        # Basic essentials to run pygame
        pygame.init()
        self.screen = pygame.display.set_mode((Length, Width))
        pygame.display.set_caption('Knights, Archers and Ghasts')
        self.clock = pygame.time.Clock()
        self.map = Map()

    def runSim(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.map.run()
            pygame.display.update()
            self.clock.tick(FPS)

# If its main file, create instance of the class then run it 
if __name__ == '__main__':
    sim = Sim()
    sim.runSim()
