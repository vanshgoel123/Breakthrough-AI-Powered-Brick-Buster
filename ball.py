import random 
import pygame
from conf import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"ba.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20)) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.random() * WIDTH, HEIGHT / 2)

        self.speed_x = 5
        self.speed_y = 5

    def update(self, game_manager):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
