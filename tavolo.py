import pygame
import random

mina = 'm'
vuoto = ''

class Cella:
    def __init__(self, screen, width, height, posx, posy, val='') -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.val = val

        self.coperto = True

        self.esplosa = False

        self.img_mina = pygame.image.load("Mina.png")
        self.img_mina = pygame.transform.scale(self.img_mina, (width, height))

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), int(self.height), bold = True, italic = False)

    def scopri(self):
        if not self.coperto:
            return False
        self.coperto = False

        if self.val == mina:
            self.esplosa = True

            return True


    def draw(self) -> None:
        if self.coperto:
            pygame.draw.rect(self.screen, (80, 80, 80),
                            (self.posx, self.posy, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, (40, 40, 40),
                            (self.posx, self.posy, self.width, self.height))

        pygame.draw.rect(self.screen, (120, 120, 120),
                         (self.posx, self.posy, self.width, self.height), 2)
        # print(self.posx, self.posy)
        if self.val == vuoto or self.coperto:
            return
        elif self.val == mina:
            self.screen.blit(self.img_mina, (self.posx, self.posy))

            if self.esplosa:  
                self.img_exp = pygame.image.load("Exp.png")
                self.img_exp = pygame.transform.scale(self.img_exp, (self.width, self.height))
                self.screen.blit(self.img_exp, (self.posx, self.posy))
        else:
            self.renderNumero = self.font.render(self.val, True, (230, 230, 230), None)
            x = self.posx + self.width / 2 - self.renderNumero.get_width() / 2
            y = self.posy + self.height / 2 - self.renderNumero.get_height() / 2
            self.screen.blit(self.renderNumero, (x, y))

class Griglia:
    def __init__(self, screen, width, height, offset, nrig=10, ncol=10, nmine=16) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.offset = offset
        self.nrig = nrig
        self.ncol = ncol
        self.nmine = nmine

        # self.celle = []
        # for i in range(nrig):
        #     riga = []
        #     for j in range(ncol):
        #         x = i * (width / ncol)
        #         y = j * (height / nrig)
        #         cella = Cella(screen, width/ncol, height/nrig, x, y)
        #         riga.append(cella)


        # creo le celle vuote
        self.celle = [[Cella(screen, width/ncol, height/nrig, j * (width/ncol) + offset[0], i * (height/nrig) + offset[1]) for j in range(ncol)] for i in range(nrig)]
        
        # metto le mine nella griglia
        for _ in range(nmine):
            i = random.randint(0, nrig-1)
            j = random.randint(0, ncol-1)

            while self.celle[i][j].val == mina:
                i = random.randint(0, nrig-1)
                j = random.randint(0, ncol-1)
            
            self.celle[i][j].val = mina
        
        print(len(self.celle), len(self.celle[0]))

        # metto i numerini intorno alle mine
        for i in range(nrig):
            for j in range(ncol):
                if self.celle[i][j].val == vuoto:
                    nmine = 0

                    for iad in range(-1, 2):
                        for jad in range(-1, 2):
                            if (iad, jad) != (0, 0) and i+iad >= 0 and i+iad < nrig and j+jad >= 0 and j+jad < ncol:
                                
                                if self.celle[i+iad][j+jad].val == mina:
                                    nmine += 1

                    if nmine != 0:
                        self.celle[i][j].val = str(nmine)

    def draw(self):
        for riga in self.celle:
            for cella in riga:
                cella.draw()

    def click(self, x, y):
        x -= self.offset[0]
        y -= self.offset[1]
        col = (x*self.ncol) // self.width
        rig = (y*self.nrig) // self.height
        # print(rig, col)

        #partita persa


        return self.celle[rig][col].scopri()
