from pygame.math import Vector2 as vec
import pygame
from settings import * 
from astar import *
class Pacman:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.step = 1
        self.index = 0
        self.flag = True
        #self.direction = self.move(direction)
    def update(self):
        if len(self.app.astar) == 0:
            if len(self.app.coins) > 0:
                pix_coins = [self.get_pix_pos(a) for a in self.app.coins]
                ls1 = [(self.pix_pos.x-pix_coins[i][0])**2
                        +(self.pix_pos.y-pix_coins[i][1])**2 for i in range(len(self.app.coins))]
                index = ls1.index(min(ls1))
                ls = astar(self.pix_pos, self.app.coins[index], self.app.wall)
                if ls == None:
                    self.app.coins.pop(0)
                    pass
                else:
                    for a in ls:
                        self.app.astar.append(a)
                    self.end = self.app.astar[-1]
        else:
            #self.flag = False
            x = self.app.astar.pop(0)
            #print(self.app.astar)
            if x == self.end:
                self.app.astar = []
            #print(self.app.astar)
            
            self.pix_pos = vec(x[0],x[1])
            for coin in self.app.coins:
                pix_coin = self.get_pix_pos(coin)
                if self.pix_pos == pix_coin:
                    self.app.coins.remove(coin)

    def draw(self):
        pygame.draw.circle(self.app.background, PACMAN_COLOUR, 
                            (int(self.pix_pos.x),int(self.pix_pos.y)),self.app.cell_width//2-2)

    # def get_astar(self, start, end, wall):
    #     return astar(start, end, self.app.wall)

    def get_pix_pos(self, coin=None):
        if coin == None:
            return vec(self.grid_pos.x*self.app.cell_width+self.app.cell_width//2,
                    self.grid_pos.y*self.app.cell_height+self.app.cell_height//2)
        else:
            return vec(coin.x*self.app.cell_width+self.app.cell_width//2,
                    coin.y*self.app.cell_height+self.app.cell_height//2)

