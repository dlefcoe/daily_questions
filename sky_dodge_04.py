"""
sky dodge game

by: @dlefcoe


music from: https://freemusicarchive.org/genre/Instrumental

"""


# sky dodge game

# import the pygame module
import os
import pygame
import random


# import pygame locals for easier access to key coordiantes
# from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT


# define size (for screen)
WIDTH = 800
HEIGHT = 500

# loop speed
FPS = 30

# define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")

# initialise pygame
pygame.init()

# caption and background
pygame.display.set_caption("DL skydodge game")
background = pygame.image.load(os.path.join(img_folder, "space_background_01.jpg"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# load game sounds
thwack_01 = pygame.mixer.Sound(
    os.path.join(snd_folder, "thwack-1.0\\PCM\\thwack-02.wav")
)
thwack_02 = pygame.mixer.Sound(
    os.path.join(snd_folder, "thwack-1.0\\PCM\\thwack-03.wav")
)
soundFile = os.path.join(snd_folder, "Chad_Crouch_-_Algorithms.mp3")
soundFile_LastEnemy = os.path.join(snd_folder, "WHY_-_02_-_crashlanding_in_gaza.mp3")
pygame.mixer.music.load(soundFile)

# play sound
pygame.mixer.music.play(loops=-1)

# text message to player
font = pygame.font.SysFont("monospace", 12)
text = font.render("sky dodge text", True, WHITE, BLACK)
textRect = text.get_rect()
textRect.center = (int(WIDTH * 0.60), int(HEIGHT * 0.05))
textRect02 = text.get_rect()
textRect02.center = (int(WIDTH * 0.60), int(HEIGHT * 0.07))


class Player(pygame.sprite.Sprite):
    """class for player sprite"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(DARKRED)
        imageName = [
            "marsRocket_01.jpg",
            "retro_aircraft_01.png",
            "DL-rocket-red-01.png",
        ]
        self.image = pygame.image.load(os.path.join(img_folder, imageName[2])).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (int(WIDTH * 0.25), int(HEIGHT / 2))
        self.x_speed = 4
        self.y_speed = 0
        # self.scale = 50

    def update(self):
        """update the player"""
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # dont get to close to top or bottom
        if self.rect.bottom > HEIGHT - 10:
            self.y_speed = -3
        if self.rect.top < 10:
            self.y_speed = 1
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH


class Enemy(pygame.sprite.Sprite):
    """class for enemy sprite"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        imageName = [
            "dl-rocket-orange-up-01.png",
            "dl-rocket-green-up-01.png",
            "dl-rocket-pink-up-01.png",
            "dl-rocket-cyan-up-01.png",
            "dl-rocket-brown-up-01.png",
            "dl-rocket-purple-up-01.png",
        ]
        self.image = pygame.image.load(
            os.path.join(img_folder, random.choice(imageName))
        ).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (int(WIDTH * 0.95), int(HEIGHT * 0.5))
        # self.rect.size
        self.x_speed = random.randint(-2, 2)
        self.y_speed = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # dont get to close to top or bottom
        if self.rect.bottom > HEIGHT - 10:
            self.y_speed = -2
        if self.rect.top < 10:
            self.y_speed = 1
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH


# setup the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# initialise player
player = Player()


# make list of ememies
enemy = []

numEnemies = 10
for i in range(numEnemies):
    enemy.append(Enemy())
    enemy[i].rect.center = (
        int(WIDTH * random.uniform(0.25, 0.95)),
        int(HEIGHT * random.uniform(0.1, 0.95)),
    )


all_sprites.add(player, enemy)


# run until the user asks to quit
running = True
countCrash = 0
speedLimit = 20
while running:
    # keep loop running at correct speed
    clock.tick(FPS)

    # mouse position
    mousePosition = pygame.mouse.get_pos()

    # head towards mouse, but not too quickly
    if mousePosition[0] > player.rect.center[0] and player.x_speed < speedLimit:
        player.x_speed = int((mousePosition[0] - player.rect.center[0]) / 10)
    if mousePosition[0] < player.rect.center[0] and player.x_speed > -speedLimit:
        player.x_speed = int((mousePosition[0] - player.rect.center[0]) / 10)
    if mousePosition[1] > player.rect.center[1] and player.y_speed < speedLimit:
        player.y_speed = int((mousePosition[1] - player.rect.center[1]) / 10)
    if mousePosition[1] < player.rect.center[1] and player.y_speed > -speedLimit:
        player.y_speed = int((mousePosition[1] - player.rect.center[1]) / 10)

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
            # escape key pressed
            if event.key == pygame.K_ESCAPE:
                running = False

    # position label
    text = font.render(
        "enemy[0] distance measure x, y: "
        + str(player.rect.center[0] - enemy[0].rect.center[0])
        + ", "
        + str(player.rect.center[1] - enemy[0].rect.center[1]),
        True,
        WHITE,
        BLACK,
    )
    text01 = font.render("number of enemies: " + str(numEnemies), True, WHITE, BLACK)

    # collision occurs
    collisionRadius = 50
    if (
        abs(player.rect.center[0] - enemy[0].rect.center[0]) < collisionRadius
        and abs(player.rect.center[1] - enemy[0].rect.center[1]) < collisionRadius
    ):
        print("enemy count crash:", numEnemies)
        thwack_01.play()
        thwack_02.play(2)

        # reduce number of enemies
        # enemy.pop()
        enemy[numEnemies - 1].image.fill(BLACK)
        enemy[numEnemies - 1].image.set_colorkey(BLACK)
        numEnemies = numEnemies - 1

        # 1 enemy left
        if numEnemies < 2:
            pygame.mixer.music.load(soundFile_LastEnemy)
            pygame.mixer.music.play()

        # no enemies left
        if numEnemies < 1:
            text01 = font.render("game over", True, WHITE, BLACK)
            # exit game
            running = False

        imageName = [
            "dl-rocket-orange-up-01.png",
            "dl-rocket-green-up-01.png",
            "dl-rocket-pink-up-01.png",
            "dl-rocket-cyan-up-01.png",
            "dl-rocket-brown-up-01.png",
        ]
        # make new list of enemies
        for i in range(numEnemies):
            enemy[i].rect.center = (
                int(WIDTH * random.uniform(0.25, 0.95)),
                int(HEIGHT * random.uniform(0.05, 0.95)),
            )
            enemy[i].image = pygame.image.load(
                os.path.join(img_folder, random.choice(imageName))
            ).convert()
            enemy[i].image.set_colorkey(WHITE)

    # update
    all_sprites.update()

    # draw background image and sprites
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # write text
    screen.blit(text, textRect)
    screen.blit(text01, textRect02)

    # flip display
    pygame.display.flip()

# done. time to quit.
pygame.quit()
