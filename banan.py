import sys, pygame, time, os
pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode((size), pygame.RESIZABLE)
yellow = 255,255,0
banana = pygame.image.load("pygame/Single-Banana-PNG.png")
bananarect = banana.get_rect()
clicked = 0
my_font = pygame.font.SysFont('Comic Sans MS', 30)
counter = my_font.render(f'0', False, (0,0,0))
counterrect = counter.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed(3):
                clicked += 1
                counter = my_font.render(f'{clicked}', False, (0,0,0))
    screen.fill(yellow)
    screen.blit(banana, bananarect)
    screen.blit(counter, counterrect)
    pygame.display.flip()