import pygame, sys
from pygame.locals import *
import os
basedir = os.path.abspath(os.path.dirname(__file__))
pygame.init()

FPS = 50
fpsClock = pygame.time.Clock()

#set up window
DISPLAYSURF = pygame.display.set_mode((1000,750), 0, 32) # .convert_alpha()
pygame.display.set_caption("Animation")

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
catImg = pygame.image.load(os.path.join(basedir,"cat.png")).convert_alpha()
catImg.set_alpha(128)
catx = 10
caty = 10
direction = 'right'

DISPLAYSURF.fill(WHITE)

#pygame.mixer.music.load('venus.mp3')
#pygame.mixer.music.play(-1,0.0)

positions = []


def handle_mouse_move(catx, caty, mousepos):
    mousex, mousey = mousepos
    #normalise mousex/y for size of cat image (125 x 79)
    mousex-=79/2
    mousey-=125/2
    newcatx = catx + (mousex - catx) / 10
    newcaty = caty + (mousey - caty) / 10
    return (newcatx, newcaty)


def move_cat(x,y, positions):
    positions.append((x, y))
    if len(positions) > 50:
        positions = positions[1:]
    return positions


fontObj = pygame.font.Font('freesansbold.ttf', 24)
textSurfaceObjUp = fontObj.render('UP', True, GREEN, BLUE)
textSurfaceObjDown = fontObj.render('DOWN', True, GREEN, BLUE)
textSurfaceObjLeft = fontObj.render('LEFT', True, GREEN, BLUE)
textSurfaceObjRight = fontObj.render('RIGHT', True, GREEN, BLUE)

while True:
    DISPLAYSURF.fill(WHITE)

    #fontObj = pygame.font.Font('freesansbold.ttf', 6+(int((catx+caty)/5)))
    #textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
    #textRectObj = textSurfaceObj.get_rect()
    #textRectObj.center = (200, 150)
    #DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    #pygame.draw.line(DISPLAYSURF, BLUE, (0,0), (400,300), 100)

    events = pygame.event.get()
    if len(events):
        for event in events:
            if event.type == QUIT:
                soundObj = pygame.mixer.Sound(os.path.join(basedir, 'stop.wav'))
                soundObj.play()
                fpsClock.tick(1)
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                catx, caty = handle_mouse_move(catx, caty, event.pos)
                positions.append((catx, caty))
                if len(positions) > 50:
                    positions = positions[1:]
    else:
        if len(positions) > 1:
            positions = positions[1:]

    alpha = 0 # -(float(360.0 / 50)) # *len(positions))
    for pos in positions:
        alpha_cat = catImg.copy()
        # alpha_cat.set_alpha(alpha)
        DISPLAYSURF.blit(pygame.transform.rotate(alpha_cat, alpha), pos)
        alpha -= float(360.0 / 50.0)

    if (pygame.key.get_pressed()[pygame.K_UP]):
        caty -= 10
        rect = textSurfaceObjUp.get_rect()
        rect.center = (catx, caty)
        DISPLAYSURF.blit(textSurfaceObjUp, rect)
        positions = move_cat(catx, caty, positions)

    if (pygame.key.get_pressed()[pygame.K_DOWN]):
        caty+=10
        rect = textSurfaceObjDown.get_rect()
        rect.center = (catx, caty)
        DISPLAYSURF.blit(textSurfaceObjDown, rect)
        positions = move_cat(catx, caty, positions)

    if (pygame.key.get_pressed()[pygame.K_LEFT]):
        catx-=10
        rect = textSurfaceObjLeft.get_rect()
        rect.center = (catx, caty)
        DISPLAYSURF.blit(textSurfaceObjLeft, rect)
        positions = move_cat(catx, caty, positions)

    if (pygame.key.get_pressed()[pygame.K_RIGHT]):
        catx+=10
        rect = textSurfaceObjRight.get_rect()
        rect.center = (catx, caty)
        DISPLAYSURF.blit(textSurfaceObjRight, rect)
        positions = move_cat(catx, caty, positions)

    print (len(positions))
    pygame.display.update()
    fpsClock.tick(FPS)
    #FPS += 1
