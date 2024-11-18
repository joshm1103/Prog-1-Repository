import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_one = (event.pos[0] // 32) * 32
                    click_two = (event.pos[1] // 32) * 32

                    if click_one == x and click_two == y:
                        x = (random.randrange(0, 640) // 32) * 32
                        y = (random.randrange(0, 512) // 32) * 32
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            a = 32
            b = 32
            while a <= 640:
                pygame.draw.line(screen, (0, 0, 0), (a, 0), (a, 640))
                a += 32
            while b <= 640:
                pygame.draw.line(screen, (0, 0, 0), (0, b), (640, b))
                b += 32
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
