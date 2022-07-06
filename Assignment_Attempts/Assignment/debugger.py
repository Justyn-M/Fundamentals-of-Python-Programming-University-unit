import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debugger(info, y = 10, x = 10):
    surfaceDisplay = pygame.display.get_surface()
    surfaceDebug = font.render(str(info), True, 'White')
    rectDebug = surfaceDebug.get_rect(topleft = (x,y))
    pygame.draw.rect(surfaceDisplay, 'Black', rectDebug)
    surfaceDisplay.blit(surfaceDebug, rectDebug)
