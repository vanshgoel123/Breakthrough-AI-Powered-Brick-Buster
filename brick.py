import random 
import pygame
from conf import *

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(WHITE) 
        pygame.draw.rect(self.image, random.choice(BRICK_COLORS), pygame.Rect(2, 2, BRICK_WIDTH-4, BRICK_HEIGHT-4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
