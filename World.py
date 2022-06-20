import pygame
from Cell import Cell

# setting which cells will be neighbors
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

# defining a World class
class World:
    def __init__(self, screen, path, WIDTH, HEIGHT, revive_nbh, alive_nbh):
        self.screen = screen
        self.reviveNbh = revive_nbh
        self.aliveNbh = alive_nbh
        
        # reading file data
        with open(path, 'r') as f:
            data = [[int(cell) for cell in line.split(' ')] for line in f]
        
        # setting the appropriate size of cells
        self.data = []
        w = WIDTH / len(data[0])
        h = HEIGHT / len(data)
        self.cellsGroup = pygame.sprite.Group()
        Cell.set_images_sizes(w, h)
        
        edgeCell = Cell(0, -w, -h)
        
        # the top row of helper cells
        self.data.append([])
        for i in range(len(data[0])+2):
            self.data[0].append(edgeCell)
        
        # cells on the board and side rows of helper cells
        for i in range(len(data)):
            self.data.append([])
            self.data[i+1].append(edgeCell)
            for j in range(len(data[i])):
                c = Cell(data[i][j], w/2 + j*w, h/2 + i*h)
                self.data[i+1].append(c)
                self.cellsGroup.add(c)
            self.data[i + 1].append(edgeCell)
        
        # bottom row of helper cells
        self.data.append([])
        for i in range(len(data[0]) + 2):
            self.data[len(data)+1].append(edgeCell)
            
        # calculating next states
        self.calculateNextStates()

    # tick - function responsible for events that are to happen in the next frame
    def tick(self):
        self.update()
        self.cellsGroup.draw(self.screen)
        self.calculateNextStates()
        
        
    # updating each cell
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
                # if a dead cell has enough neighbors it becomes alive
                if nbh_num in self.reviveNbh:
                    self.data[i][j].setNextState(1)
                # if a living cell doesn't have enough neighbors it becomes dead
                elif nbh_num not in self.aliveNbh:
                    self.data[i][j].setNextState(0)
                    
    # getter to date
    def get_data(self):
        return self.data
