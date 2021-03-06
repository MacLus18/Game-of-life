import pygame

class Cell(pygame.sprite.Sprite):

    def set_images_sizes(w, h):
        for i in range(len(Cell.states)):
            Cell.states[i] = pygame.transform.scale(Cell.states[i], (w,h))

    states = [pygame.image.load('images/empty_cell.jpg'), pygame.image.load('images/cell.jpg')]

    def __init__(self, startState, x, y):
        super().__init__()
        self.state = self.nextState = startState
        self.image = Cell.states[self.state]
        self.rect = self.image.get_rect(center=(x, y))

    def setNextState(self, nextState):
        self.nextState = nextState
    
    def update(self):
        self.state = self.nextState
        self.image = Cell.states[self.state]
        
    def changeState(self):
        self.state = (self.state + 1) % len(Cell.states)
        self.image = Cell.states[self.state]
        
