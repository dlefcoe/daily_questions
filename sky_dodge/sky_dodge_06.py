"""
sky dodge game

original version: somewhere around 2020
current version: September 2025

by: @dlefcoe


music from: https://freemusicarchive.org/genre/Instrumental

"""
# sky dodge game

# import the pygame module
import os
import pygame
import random

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


class Game:
    def __init__(self):
        """Initialize pygame and game state"""
        pygame.init()

        # caption and background
        pygame.display.set_caption("DL skydodge game")
        self.background = pygame.image.load(
            os.path.join(img_folder, "space_background_01.jpg")
        )
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        # load game sounds
        self.thwack_01 = pygame.mixer.Sound(
            os.path.join(snd_folder, "thwack-1.0\\PCM\\thwack-02.wav")
        )
        self.thwack_02 = pygame.mixer.Sound(
            os.path.join(snd_folder, "thwack-1.0\\PCM\\thwack-03.wav")
        )
        self.soundFile = os.path.join(snd_folder, "Chad_Crouch_-_Algorithms.mp3")
        self.soundFile_LastEnemy = os.path.join(
            snd_folder, "WHY_-_02_-_crashlanding_in_gaza.mp3"
        )
        pygame.mixer.music.load(self.soundFile)
        pygame.mixer.music.play(loops=-1)

        # text message to player
        self.font = pygame.font.SysFont("monospace", 12)
        self.textRect = self.font.render("sky dodge text", True, WHITE, BLACK).get_rect()
        self.textRect.center = (int(WIDTH * 0.60), int(HEIGHT * 0.05))
        self.textRect02 = self.font.render("sky dodge text", True, WHITE, BLACK).get_rect()
        self.textRect02.center = (int(WIDTH * 0.60), int(HEIGHT * 0.07))

        # setup the drawing window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()

        # initialise player
        self.player = Player()

        # initialise multiple enemies
        # self.all_sprites = pygame.sprite.Group()

        # initialise enemies
        self.enemy = []
        self.numEnemies = 10
        for i in range(self.numEnemies):
            e = Enemy()
            e.rect.center = (
                int(WIDTH * random.uniform(0.25, 0.95)),
                int(HEIGHT * random.uniform(0.1, 0.95)),
            )
            self.enemy.append(e)

        self.all_sprites.add(self.player, self.enemy)

        # state
        self.running = True
        self.countCrash = 0
        self.speedLimit = 20

    def process_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                key_press:int = event.key
                if key_press == pygame.K_DOWN:
                    self.player.y_speed += 1
                if key_press == pygame.K_UP:
                    self.player.y_speed -= 1
                if key_press == pygame.K_LEFT:
                    self.player.x_speed -= 1
                if key_press == pygame.K_RIGHT:
                    self.player.x_speed += 1
                if key_press == pygame.K_ESCAPE:
                    self.running = False

    def update_player_movement(self):
        """Move player toward mouse position (with speed limits)"""
        mousePosition = pygame.mouse.get_pos()
        if mousePosition[0] > self.player.rect.center[0] and self.player.x_speed < self.speedLimit:
            self.player.x_speed = int((mousePosition[0] - self.player.rect.center[0]) / 10)
        if mousePosition[0] < self.player.rect.center[0] and self.player.x_speed > -self.speedLimit:
            self.player.x_speed = int((mousePosition[0] - self.player.rect.center[0]) / 10)
        if mousePosition[1] > self.player.rect.center[1] and self.player.y_speed < self.speedLimit:
            self.player.y_speed = int((mousePosition[1] - self.player.rect.center[1]) / 10)
        if mousePosition[1] < self.player.rect.center[1] and self.player.y_speed > -self.speedLimit:
            self.player.y_speed = int((mousePosition[1] - self.player.rect.center[1]) / 10)

    def handle_collisions(self):
        """Check and handle collisions with enemies"""
        collisionRadius = 50
        my_enemy: Enemy = self.enemy[0]
        if (
            abs(self.player.rect.center[0] - my_enemy.rect.center[0]) < collisionRadius
            and abs(self.player.rect.center[1] - my_enemy.rect.center[1]) < collisionRadius
        ):
            print("enemy count crash:", self.numEnemies)
            self.thwack_01.play()
            self.thwack_02.play(2)

            # reduce number of enemies
            my_enemy: Enemy = self.enemy[self.numEnemies - 1]
            my_enemy.image.fill(BLACK)
            my_enemy.image.set_colorkey(BLACK)
            self.numEnemies -= 1

            # 1 enemy left
            if self.numEnemies < 2:
                pygame.mixer.music.load(self.soundFile_LastEnemy)
                pygame.mixer.music.play()

            # no enemies left
            if self.numEnemies < 1:
                self.text01 = self.font.render("game over", True, WHITE, BLACK)
                self.running = False
                return

            # reset enemy positions and images
            imageName = [
                "dl-rocket-orange-up-01.png",
                "dl-rocket-green-up-01.png",
                "dl-rocket-pink-up-01.png",
                "dl-rocket-cyan-up-01.png",
                "dl-rocket-brown-up-01.png",
            ]
            for i in range(self.numEnemies):
                self.enemy[i].rect.center = (
                    int(WIDTH * random.uniform(0.25, 0.95)),
                    int(HEIGHT * random.uniform(0.05, 0.95)),
                )
                self.enemy[i].image = pygame.image.load(
                    os.path.join(img_folder, random.choice(imageName))
                ).convert()
                self.enemy[i].image.set_colorkey(WHITE)

    def update(self):
        """Update game state"""
        self.update_player_movement()
        self.handle_collisions()
        self.all_sprites.update()

    def draw(self):
        """Draw everything"""
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)

        # labels
        text = self.font.render(
            "enemy[0] distance measure x, y: "
            + str(self.player.rect.center[0] - self.enemy[0].rect.center[0])
            + ", "
            + str(self.player.rect.center[1] - self.enemy[0].rect.center[1]),
            True,
            WHITE,
            BLACK,
        )
        text01 = self.font.render(
            "number of enemies: " + str(self.numEnemies), True, WHITE, BLACK
        )
        self.screen.blit(text, self.textRect)
        self.screen.blit(text01, self.textRect02)

        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            self.clock.tick(FPS)
            self.process_events()
            self.update()
            self.draw()

        pygame.quit()


# Run the game
Game().run()

