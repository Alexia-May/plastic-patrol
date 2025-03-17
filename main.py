import sys
import pygame
import random
import time
import math
from settings import Settings
from user import User
from sealife import Fish
from plastics import Plastic
from button import Button

class PlasticPatrol:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.user = User(self)
        self.fishes = pygame.sprite.Group()

        self.distance = 0

        self.plastics = pygame.sprite.Group()
        self.background = pygame.transform.scale(pygame.image.load('assets/underwater.png'), (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Plastic Patrol")
        # Game states
        self.game_active = False  # Track whether the game is running
        self.button = Button(self, "Start")  # Create a start button

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.fishes.update()
                self.plastics.update()
                self.user.update()
                self._load_fish()
                self._delete_fish()
                self._load_plastic()
                self._delete_plastic()
                self._collision() 
                self._score()
                self._lives()
                self.end_game()

            self._update_screen()
            self.clock.tick(60)



    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Movements of the net controlled by the player
            elif event.type == pygame.KEYDOWN and self.game_active:
                # When a key is pressed
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = True
                    self.user.facing_right = True
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = True
                    self.user.facing_right = False
                elif event.key == pygame.K_DOWN:
                    self.user.moving_down = True
                elif event.key == pygame.K_UP:
                    self.user.moving_up = True
                # When the keys are not pressed
            elif event.type == pygame.KEYUP and self.game_active:
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = False
                elif event.key == pygame.K_UP:
                    self.user.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.user.moving_down = False
                # Using the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.rect.collidepoint(mouse_pos) and not self.game_active:
                    # Start the game
                    self.time_started = time.time
                    self.game_active = True

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.screen.blit(self.background, game.screen.get_rect())

        if self.game_active:
            for fish in self.fishes.sprites():
                fish.draw_fish()
            for plastic in self.plastics.sprites():
                plastic.draw_plastic()
            self.user.blitme()
            # self.user.draw_hitbox() #enable to debug john collision box
            self._score()
            self._lives()
            
        else:
            self.button.draw()  # Draw the start button when the game is inactive
        pygame.display.flip()
    
    def _load_fish(self):
        if random.randint(0, self.settings.fish_load) == 3:
            new_fish = Fish(self)
            self.fishes.add(new_fish)
        self.settings.fish_speed
        self.settings.fish_speed =  1 + self.distance / 1000
        self.settings.plastic_speed = 1+  self.distance / 1000 
        if self.settings.fish_load > 10:
            self.settings.fish_load = 100 -  10 * math.ceil(self.distance / 1000) 

    def _delete_fish(self):
        for fish in self.fishes.copy():
            if fish.rect.bottom <= 0:
                self.fishes.remove(fish)

#Plastics
    def _load_plastic(self):
        if random.randint(0,200) == 3:
            new_plastic = Plastic(self)
            self.plastics.add(new_plastic)

    def _delete_plastic(self):
        for plastic in self.plastics.copy():
            if plastic.rect.bottom <= 0:
                self.plastics.remove(plastic)
    
    def _collision(self):
    # Custom collision function for circular hitbox
        def circle_collision(user, sprite):
        # Calculate the distance between the circle center and the sprite's rect center
            distance = ((user.circle_center[0] - sprite.rect.centerx) ** 2 +
                        (user.circle_center[1] - sprite.rect.centery) ** 2) ** 0.5
            return distance < user.circle_radius + max(sprite.rect.width, sprite.rect.height) / 2

    # Check collision with fishes
        if pygame.sprite.spritecollide(self.user, self.fishes, True, collided=circle_collision):
            self.settings.user_lives -= 1

    # Check collision with plastics
        if pygame.sprite.spritecollide(self.user, self.plastics, True, collided=circle_collision):
            self.settings.user_score += 10
    

    # def _score(self):
    #     self.distance += self.settings.speed
    #     font = pygame.font.Font(None, 36)  # Use default font, size 36
    #     distance_text = font.render(f"Points: {self.distance}", True, (255, 255, 255))  # White color
    #     self.screen.blit(distance_text, (10, 10))  # Top-left corner

    def _lives(self):
        font = pygame.font.Font(None, 36) 
        lives_display = font.render(f"Lives: {self.settings.user_lives}", True, (255, 255, 255))  # White color
        self.screen.blit(lives_display, (10, 10))  # Top-left corner

    def _score(self):
        font = pygame.font.Font(None, 36) 
        score_display = font.render(f"Score: {self.settings.user_score}", True, (255, 255, 255))  # White color
        self.screen.blit(score_display, (750, 10))  # Top-left corner

    def end_game(self):
        if self.settings.user_lives < 1:
            print("THIS SHOULD BE GAME OVER")
            font = pygame.font.Font(None, 74)  # Create a font object (None uses default font)
            game_over_text = font.render(f"Game Over", True, (255, 0, 0))  # Render the text in red
            score_text = font.render(f"Score: {self.settings.user_score}", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
            score_rect = score_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 1.7))
            self.screen.blit(game_over_text, game_over_rect)  # Draw text at the center of the screen
            self.screen.blit(score_text, score_rect)  # Draw text at the center of the screen
            pygame.display.flip()
            pygame.time.delay(3000)  # Pause for 3 seconds before exiting

            self.distance = 0
            self.user.rect.y = 1
            self.user.moving_left = False
            self.user.moving_right = False
            self.user.moving_up = False
            self.user.moving_down = False
            self.settings.reset_game()
            self.game_active = False
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = PlasticPatrol()
    game.run_game()
