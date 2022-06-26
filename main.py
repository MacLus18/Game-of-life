import pygame
import os
from World import World

pygame.init()

SIZE = WIDTH, HEIGHT = 300, 300
FPS = 10
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()
running = True
pause = True

worlds_dir = 'worlds'
worlds = os.listdir(worlds_dir)
for num, world in enumerate(worlds):
    print(str(num)+'.', world)

chosen_world = int(input('Enter the number of the world to be opened: '))
game = World(screen, 'worlds/'+worlds[chosen_world],WIDTH, HEIGHT, [3], [2, 3])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause is False:
                    game.calculateNextStates()
        
         

    screen.fill((128,128,128))
    if not pause:
        game.tick()
    game.draw()
    pygame.display.update()

    clock.tick(FPS)

save_name = input('Save world as or click [Enter] to not save: ')
if save_name != '':
    path = 'worlds/' + save_name + '.txt'
    
    with open(path, 'w') as f:
        data = game.get_data()
        
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                f.write(str(data[i][j].state) + ' ')
            f.write('\n')
            
pygame.quit()
