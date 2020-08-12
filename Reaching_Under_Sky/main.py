import pygame
import random
import math
import time

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((500, 800))

# title and icon
pygame.display.set_caption("Reaching-Under-Sky")
icon = pygame.image.load('mainSheep(64).png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('background500x800.jpg')

# cloud list
cloud_list = []

# time
time = 0

# clock
clock = pygame.time.Clock()


# initial speed
speed = 3

# clouds
class clouds:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = 680
        self.width = random.randint(120, 160)
        self.cloud = pygame.Surface((self.width,20))

    # build cloud
    def built(self):
        pygame.draw.rect(self.cloud,(100,100,100),[0,0,self.width,20],30)
        self.rect = self.cloud.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self):
        self.cloud = pygame.image.load('cloud (1).png')
        self.cloud.convert()
        screen.blit(self.cloud, self.rect.center)

    def update(self):
        # check boarder for clouds
        if self.x <= 0:
            self.x = 0
        elif self.x >= 380:
            self.x = 380

        self.y -= speed

# player
class players:
    def __init__(self):
        self.x = cloud_list[0].x + 50
        self.y = 630
        self.player = pygame.Surface((50, 55))
        self.up = False
        self.score = 0

    # build player
    def built(self):
        pygame.draw.rect(self.player, (255, 255, 255), [self.x, self.y, 50, 55], 30)
        self.rect = self.player.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self):
        self.player = pygame.image.load('mainSheep(64).png')
        self.player.convert()
        screen.blit(self.player, self.rect.center)

    # checking if player is on the cloud
    def y_update(self):
        self.up = False
        for i in cloud_list:
            if 40 < i.y - self.y < 55 and (i.x - 40) <= self.x <= (i.x + i.width - 10):
                self.up = True
                if player.gameOver() == False:
                    self.score += 1/30

    def displayScore(self):
        font = pygame.font.Font('freesansbold.ttf', 24)
        self.scoreDisplay = font.render(str(int(self.score)), True, (200, 129, 0))
        screen.blit(self.scoreDisplay, (450, 18))

        if self.up:
            self.y -= speed
        else:
            self.y += speed

    # key movement
    def x_update(self):
        # key control
        keys = pygame.key.get_pressed()  #
        if player.gameOver() == False:
            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                pass
            elif keys[pygame.K_LEFT]:
                self.x -= 6
            elif keys[pygame.K_RIGHT]:
                self.x += 6

        # setting X boundaries
        if self.x <= -10:
            self.x = -10
        elif self.x >= 456:
            self.x = 456

    def gameOver(self):
        if self.y <= 0 or self.y >= 800:
            font = pygame.font.Font('freesansbold.ttf', 30)
            screen.fill((202, 87, 0))
            self.gameoverDisplay = font.render("GAME OVER   |   SCORE: " + str(int(self.score)), True, (250, 250, 250))
            screen.blit(self.gameoverDisplay, (45, 380))
            return True
        else:
            return False

# create cloud
cloud = clouds()
cloud_list.append(cloud)

# crate player
player = players()

# game loop
running = True
while running:
    # background
    screen.blit(background, (0, 0))

    # close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    # counting time
    time += 1
    clock.tick(60)

    # speed up
    if speed <= 9:
        if time % 600 == 0:
            speed += 0.7

    # calculate time for amount of cloud to draw
    cloudDrawTime = int(180 / speed)

    if player.gameOver() == False:
        # add cloud
        if time % cloudDrawTime == 0:
            cloud = clouds()
            cloud_list.append(cloud)
        # draw cloud every layer of Y
        for i in cloud_list:
            i.update()
            if i.y < 0:
                cloud_list.remove(i)
            i.built()
            i.draw()

    player.x_update()
    player.y_update()
    player.displayScore()
    player.built()
    player.draw()
    player.gameOver()
    pygame.display.update()
