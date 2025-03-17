import pygame
from random import randint
from pygame.sprite import Sprite

class Plastic(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # self.colour = self.settings.life_colour
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load('assets/plastic.png'), (50, 50))

        self.rect = self.image.get_rect()  
        self.rect.midtop = (randint(0,900), 0)
        self.y = float(self.rect.y)

    # Plastic movement
    def update(self): 
        self.y += self.settings.plastic_speed
        self.rect.y = self.y

    def draw_plastic(self):
        # pygame.draw.rect(self.screen, self.image, self.rect)
        self.screen.blit(self.image, self.rect)



        

