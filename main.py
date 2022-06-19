import pygame
from classes.World import World

pygame.init()

SIZE = WIDTH, HEIGHT = 300, 300
FPS = 10

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()
running = True

path = 'worlds/' + input('Enter the name of the world to be opened: ') + '.txt'
w = World(screen, path ,WIDTH, HEIGHT, [3], [2, 3])
#w.show_world()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,128,128))
    w.tick()
    pygame.display.update()

    clock.tick(FPS)

save_name = input('Save world as or click [Enter] to not save: ')
if save_name != '':
    path = 'worlds/' + save_name + '.txt'
    with open(path, 'w') as f:
        for i in range(1, len(w.data) - 1):
            for j in range(1, len(w.data[i]) - 1):
                f.write(str(w.data[i][j].state) + ' ')
            f.write('\n')
pygame.quit()