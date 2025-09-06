# sky dodge game

# import the pygame library
import os
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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (100, 100, 255)
DARKRED = (100, 0, 0)
WHITE = (255, 255, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')

# initialise pygame
pygame.init()

pygame.display.set_caption('DL skydodge game')

# load game sounds
thwack_01 = pygame.mixer.Sound(os.path.join(snd_folder, 'thwack-1.0\\PCM\\thwack-02.wav'))

# play sound
thwack_01.play()

# text message to player
font = pygame.font.SysFont('monospace',12)
text = font.render('sky dodge text', True, WHITE, BLACK)
textRect = text.get_rect()
textRect.center = (WIDTH*0.60, HEIGHT*0.05)
textRect02 = text.get_rect()
textRect02.center = (WIDTH*0.60, HEIGHT*0.07)


# play a sound


class Player(pygame.sprite.Sprite):
    ''' class for player sprite '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(DARKRED)
        imageName = ['marsRocket_01.jpg', 'retro_aircraft_01.png']
        self.image = pygame.image.load(os.path.join(img_folder, imageName[1])).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*0.25, HEIGHT / 2)
        self.x_speed = 5
        self.y_speed = 0
        self.scale = 75

    def update(self):
        ''' update the player '''
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.image = pygame.transform.scale(self.image,(self.scale,self.scale))

        # dont get to close to top or bottom
        if self.rect.bottom > HEIGHT - 10:
            self.y_speed = -3
        if self.rect.top < 10:
            self.y_speed = 1
        if self.rect.left > WIDTH:
            self.rect.right = 0
            

class Enemy(pygame.sprite.Sprite):
    ''' class for player sprite '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        imageName = ['marsRocket_01.jpg', 'retro_aircraft_01.png', 'spaceship_24px.png', 'flaticon_rocket_512px.png']
        self.image = pygame.image.load(os.path.join(img_folder, imageName[3])).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*0.95, HEIGHT*0.50)
        self.x_speed = 0
        self.y_speed = 0
        self.scale = 50 # scale the image size

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.image = pygame.transform.scale(self.image,(self.scale,self.scale))

#setup the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()


enemy = Enemy()
enemy.rect.center = (WIDTH*1.25, HEIGHT*1.0)
enemySmall = Enemy()

enemySmall.rect.center = (WIDTH*1.0, HEIGHT*0.75)
enemySmall.scale = 20

all_sprites.add(player, enemy, enemySmall)

# run until the user asks to quit
running = True
countCrash = 0
while running:

    # keep loop running at correct speed
    clock.tick(FPS)

    # events in pygame
    for event in pygame.event.get():
        # user clicks close window
        if event.type == pygame.QUIT:
            running = False
        # key is pressed
        if event.type == pygame.KEYDOWN:
            # down arrow pressed
            if event.key == pygame.K_DOWN:
                player.y_speed += 1
            # up arrow pressed
            if event.key == pygame.K_UP:
                player.y_speed -= 1
            # left arrow pressed
            if event.key == pygame.K_LEFT:
                player.x_speed -= 1
            # right arrow pressed
            if event.key == pygame.K_RIGHT:
                player.x_speed += 1

    # position label
    text = font.render('enemySmall distance measure x, y: ' + str(player.rect.x - enemySmall.rect.x) + ', ' + str(player.rect.y - enemySmall.rect.y), True, WHITE, BLACK)
    text01 = font.render('enemyLarge distance measure x, y: ' + str(player.rect.x - enemy.rect.x) + ', ' + str(player.rect.y - enemy.rect.y), True, WHITE, BLACK)

    # collision occurs
    if abs(player.rect.x - enemySmall.rect.x) < 50 and abs(player.rect.y - enemySmall.rect.y) < 20:
        print('condition reached')
        thwack_01.play()

    if abs(player.rect.x - enemySmall.rect.x) <50 and abs(player.rect.y - enemySmall.rect.y) < 30:
        countCrash += 1
        text = font.render('count crash: ' + str(countCrash), True, WHITE, BLACK)
        thwack_01.play()
        

    
    



    # update
    all_sprites.update()

    # draw / render
    screen.fill(LIGHTBLUE) # fill background light blue
    all_sprites.draw(screen)

    # write text
    screen.blit(text, textRect)
    screen.blit(text01, textRect02)

    # flip display
    pygame.display.flip()

# done. time to quit.
pygame.quit()







