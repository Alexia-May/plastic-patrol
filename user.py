import pygame
from pygame.sprite import Sprite
from settings import Settings

class User:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        # Visual of the net controlled by the player
        self.image = pygame.transform.scale(pygame.image.load('assets/net.png'), (50, 50))
        self.image_flipped = pygame.transform.flip(self.image, True, False)
        self.facing_right = True
        
        # Initial location of the net
        self.rect = self.image.get_rect()  
        self.rect.center = self.screen_rect.center
        self.rect.y = 280
        self.rect.x = 300
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Initial movement of the net
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        self.circle_radius = 30  
        self.circle_offset = (self.rect.width // 2, self.rect.height // 1.3)  
        
        self.update_circle()
        
    def update_circle(self):
        # Update the circle's center based on the net's position.
        self.circle_center = (
            self.rect.x + self.circle_offset[0],
            self.rect.y + self.circle_offset[1]
        )
        
    # Net movements  
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.user_speed + (self.y/40)
            self.x += self.settings.user_speed
            
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.user_speed + (self.y/40)
            self.x -= self.settings.user_speed
        
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.user_speed + (self.x/40)
            self.y -= self.settings.user_speed
                    
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.user_speed + (self.x/40)
            self.y += self.settings.user_speed

        self.update_circle()

    #only useful for debugging
    def draw_hitbox(self):
        print(f"Circle Center: {self.circle_center}, Radius: {self.circle_radius}")
        pygame.draw.circle(
        self.screen, 
        (0, 255, 0), 
        self.circle_center, 
        self.circle_radius, 
        2 #line thickness
    )
        
        
        
    def blitme(self):
        if self.facing_right:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image_flipped, self.rect)

    def collision(self, distance):
        print(self.rect.y)
        if distance > 0:
            self.rect.y += distance
        if self.rect.y > 1:
            self.rect.y += distance
        
