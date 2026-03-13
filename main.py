import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    #Check for all events
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit() #Close Window
            quit()

            #end pygame