import pygame
from conf import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(r"paddle.png").convert_alpha()  # Load image with transparency
        self.image = pygame.transform.scale(self.image, (100, 80)) 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 5)

        self.speed = 5

    def move(self, action):
        if action == "Left":
            self.rect.x -= self.speed
        if action == "Right":
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
