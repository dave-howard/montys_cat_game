import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 50
fpsClock = pygame.time.Clock()

#set up window
DISPLAYSURF = pygame.display.set_mode((1000,750), 0, 32)
pygame.display.set_caption("Animation")

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
catImg = pygame.image.load("cat.png")
catx = 10
caty = 10
direction = 'right'

DISPLAYSURF.fill(WHITE)

pygame.mixer.music.load('venus.mp3')
pygame.mixer.music.play(-1,0.0)

positions = []

def move(catx, caty, mousepos):
    mousex, mousey = mousepos
    #normalise mousex/y for size of cat image (125 x 79)
    mousex-=79/2
    mousey-=125/2
    newcatx = catx
    newcaty = caty
    if mousex > catx:
        newcatx = catx+5
    else:
        newcatx = catx-5
    if mousey > caty:
        newcaty = caty+5
    else:
        newcaty = caty-5
    # move 5 pixels from catx,cay=ty to mousex,mousey
    return (newcatx, newcaty)


while True:
    # DISPLAYSURF.fill(WHITE)
    """
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty +=5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -=5
        if caty == 10:
            direction = 'right'
    """
    DISPLAYSURF.blit(catImg, (catx, caty))
    fontObj = pygame.font.Font('freesansbold.ttf', 6+(int((catx+caty)/5)))
    textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 150)
    #DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    #pygame.draw.line(DISPLAYSURF, BLUE, (0,0), (400,300), 100)

    for event in pygame.event.get():
        if event.type == QUIT:
            soundObj = pygame.mixer.Sound('stop.wav')
            soundObj.play()
            fpsClock.tick(1)
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            catx, caty = move(catx, caty, event.pos)
            if len(positions) > 5:
                positions = positions[1:]
            positions.append((catx, caty))
            print(positions)
    pygame.display.update()
    fpsClock.tick(FPS)
    FPS += 1
