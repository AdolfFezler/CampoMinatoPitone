from tkinter.tix import WINDOW
from tavolo import Griglia

from os import system
system("cls")

import pygame
from pygame.locals import *

pygame.init()

#impostazioni finestra
WINDOW_SIZE = (600, 750)
GRIGLIA_SIZE = (600, 600)
RESTART_SIZE = (75, 75)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Campo Minato')

clock = pygame.time.Clock()
fps = 200

blocca = False
def click_down(posx,posy,su_griglia):
    global blocca
    if su_griglia:
        if g.click(posx, posy):
            blocca = True
    else: #click sulla barra nera
        if posx > WINDOW_SIZE[0]/2-RESTART_SIZE[0]/2 and posx < WINDOW_SIZE[0]/2+RESTART_SIZE[0]/2:
            pass

fine = False
g = Griglia(screen, GRIGLIA_SIZE[0], GRIGLIA_SIZE[1], (0, (WINDOW_SIZE[1]-GRIGLIA_SIZE[1])))
g.draw()

pressed = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN and not pressed:
        pressed = True
        if not blocca:
            posx, posy = pygame.mouse.get_pos()
            # print("mousebuttondown:", posx, posy)
            # click_down(posx, posy)

    if event.type == pygame.MOUSEBUTTONUP and pressed:
        pressed = False
        if not blocca:
            posx, posy = pygame.mouse.get_pos()

            if posy > WINDOW_SIZE[1]-GRIGLIA_SIZE[1]:
                click_down(posx, posy, True)
            else:
                click_down(posx, posy, False)

            # print("mousebuttonup:", posx, posy)

    # if t.vincitore != None:
    #     fine = True
    #     if t.vincitore == Tavolo.v:
    #         print('Partita finita in pareggio')
    #     else:
    #         print(f'Vince il giocatore {t.vincitore}')

    # chiamo le draw per tutti gli elementi
    g.draw()

    pygame.draw.rect(screen, (255, 255, 255),
                    (WINDOW_SIZE[0]/2 - RESTART_SIZE[0]/2, (WINDOW_SIZE[1]-GRIGLIA_SIZE[1])/2 - RESTART_SIZE[1]/2, RESTART_SIZE[0], RESTART_SIZE[1]))

    pygame.display.flip()
    clock.tick(fps)
