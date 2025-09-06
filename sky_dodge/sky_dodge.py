# sky dodge game

# import the pygame library
import pygame

# import pygame locals for easier access to key coordiantes
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# define size
WIDTH = 800
HEIGHT = 500

# loop speed
FPS = 30

# define colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
LIGHTBLUE = (100,100,255)
DARKRED = (100,0,0)

# initialise pygame
pygame.init()

pygame.display.set_caption('DL game')

class Player(pygame.sprite.Sprite):
    ''' class for sprite '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(DARKRED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5

        if self.rect.left > WIDTH:
            self.rect.right = 0
            



#setup the drawing window
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# run until the user asks to quit
running = True
while running:

    # keep loop running at correct speed
    clock.tick(FPS)

    # did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # update
    all_sprites.update()

    # draw / render
    screen.fill(LIGHTBLUE) # fill background light blue
    all_sprites.draw(screen)

    # flip display
    pygame.display.flip()

# done. time to quit.
pygame.quit()

