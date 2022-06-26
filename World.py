import pygame
from Cell import Cell

nbh = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1, -1],
    [1, 0],
    [1, 1]
]

class World:
    def __init__(self, screen, path, WIDTH, HEIGHT, revive_nbh, alive_nbh):
        self.screen = screen
        self.reviveNbh = revive_nbh
        self.aliveNbh = alive_nbh
        
        with open(path, 'r') as f:
            data = [[int(cell) for cell in line.split(' ')] for line in f]
        
        self.data = []
        self.w = WIDTH / len(data[0])
        self.h = HEIGHT / len(data)
        self.cellsGroup = pygame.sprite.Group()
        Cell.set_images_sizes(self.w, self.h)
        
        edgeCell = Cell(0, -self.w, -self.h)
        
        self.data.append([])
        for i in range(len(data[0])+2):
            self.data[0].append(edgeCell)
        
        for i in range(len(data)):
            self.data.append([])
            self.data[i+1].append(edgeCell)
            for j in range(len(data[i])):
                c = Cell(data[i][j], self.w/2 + j*self.w, self.h/2 + i*self.h)
                self.data[i+1].append(c)
                self.cellsGroup.add(c)
            self.data[i + 1].append(edgeCell)
        
        self.data.append([])
        for i in range(len(data[0]) + 2):
            self.data[len(data)+1].append(edgeCell)
            
        self.calculateNextStates()

    def tick(self):
        self.update()
        self.calculateNextStates()
        
        
    def update(self):
        for i in range(1, len(self.data)-1):
            for j in range(1, len(self.data[i])-1):
                self.data[i][j].update()
    
    
    def calculateNextStates(self):
        for i in range(1, len(self.data)-1):
            for j in range(1, len(self.data[i])-1):
                nbh_num = 0
                for k in nbh:
                    nbh_num += self.data[i+k[0]][j+k[1]].state
                if nbh_num in self.reviveNbh:
                    self.data[i][j].setNextState(1)
                elif nbh_num not in self.aliveNbh:
                    self.data[i][j].setNextState(0)
                else:
                    self.data[i][j].setNextState(self.data[i][j].state)
                    
    def get_data(self):
        return self.data
    
    def draw(self):
        self.cellsGroup.draw(self.screen)
    
    def changeCell(self, mouseX, mouseY):
        row = int(mouseY/self.h) + 1
        col = int(mouseX/self.w) + 1
        self.data[row][col].changeState()
