#
# simScreen.py - file that runs simulation in a pygame screen
#

import pygame, sys
from utilities import *
from map import Map

class Sim:
    def __init__(self):
        # Basic essentials to run pygame
        pygame.init()
        self.screen = pygame.display.set_mode((Length, Width))
        # Screen titled as 'Knight and Ghasts'
        pygame.display.set_caption('Knights and Ghasts')
        self.clock = pygame.time.Clock()
        self.map = Map()

    def runSim(self):
        while True:
            # code that says what happens when you close pygame screen
            # e as in event
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # setting screen base layer as black
            # png map file will over layer it later
            self.screen.fill('black')
            self.map.run()
            pygame.display.updates()
            self.clock.tick(FPS)

#if its main file, create class instance then run code
if __name__ == '__main__':
    sim = Sim()
    sim.runSim()
