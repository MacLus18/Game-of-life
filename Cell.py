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

    # next state setter
    def setNextState(self, nextState):
        self.nextState = nextState
    
    # update function
    def update(self):
        self.state = self.nextState
        self.image = Cell.states[self.state]

        
