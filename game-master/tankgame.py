import pygame
# import K_ESCAPE
pygame.init()

width = 900
height = 800
size = (width, height)

screen = pygame.display.set_mode(size)

background = pygame.image.load('./game_background.png').convert()
background = pygame.transform.scale(background, (width, height))
background2 = background



def main():
    bckg_x = 0


    pygame.display.set_caption('Test Game')
    clock = pygame.time.Clock()

    # background = pygame.image.load('./game_background.png').convert()
    # background = pygame.transform.scale(background, (width, height))
    # background2 = background
    
    
    # background_size = background.get_size()
    # background_rect = background.get_rect()

    # screen = pygame.display.set_mode(size)

    character = pygame.image.load('./main_tank.png').convert_alpha(background)
    character = pygame.transform.scale(character, (100,115))

    crashed = False
    while not crashed :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        rel_x = bckg_x % background.get_rect().width
        screen.blit(background, [rel_x, 0  - background.get_rect().width])
        if rel_x > 0:
            screen.blit(background2,(rel_x , 0))
        bckg_x -= 1


        screen.blit(character, (50,500))

        pygame.display.flip()
        clock.tick(80)
    
    pygame.quit()


if __name__ == '__main__':
    main()