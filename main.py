import sys
import pygame
from menu_screen import MainMenu

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TechBasics Chaos: Morning Rush")


menu = MainMenu(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        action = menu.handle(event)
        if action == "start":
            pass

    menu.draw()
    pygame.display.flip()


if __name__ == "__main__":
    main()
