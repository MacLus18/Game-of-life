import pygame
from World import World

pygame.init()

# game window
SIZE = WIDTH, HEIGHT = 300, 300
FPS = 10
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Game of Life')

clock = pygame.time.Clock()
running = True

# initializing the game
path = 'worlds/' + input('Enter the name of the world to be opened: ') + '.txt'
game = World(screen, path ,WIDTH, HEIGHT, [3], [2, 3])

# loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,128,128))
    game.tick()
    pygame.display.update()

    clock.tick(FPS)

# saving the game
save_name = input('Save world as or click [Enter] to not save: ')
if save_name != '':
    path = 'worlds/' + save_name + '.txt'
    # opneing file
    with open(path, 'w') as f:
        data = game.get_data()
        # saving each cell
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                f.write(str(data[i][j].state) + ' ')
            f.write('\n')
            
# quiting the game
pygame.quit()
