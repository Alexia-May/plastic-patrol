import pygame
from random import randint
from pygame.sprite import Sprite

class Fish(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # self.colour = self.settings.fish_colour
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load('assets/fish1.png'), (50, 50))

        self.rect = self.image.get_rect()  
        self.rect.midright = ((0), randint(0,900))
        self.x = float(self.rect.x)

    # Fish movement
    def update(self): 
        self.x += self.settings.fish_speed
        self.rect.x = self.x

    def draw_fish(self):
        self.screen.blit(self.image, self.rect)



        

