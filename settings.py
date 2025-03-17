class Settings:
    def __init__(self):
        # self.screen_width = 560
        # self.screen_height = 900

        self.screen_width = 900
        self.screen_height = 560
        self.speed = 1
        # Sealife settings = fishes the player has to avoid collecting in the net
        self.fish_speed = 2.0
        self.fish_width = 10
        self.fish_height = 10 
        # self.fish_colour = (60, 60, 60)
        self.user_speed = 7
        self.bg_colour = (135, 206, 235)
        # Plastics settings = refuse the players has to collect with the net
        self.plastic_speed = 2.0
        self.plastic_width = 10
        self.plastic_height = 10 
        # self.plastic_colour = (152, 251, 152)
        self.fish_load = 100
         # Initial lives and score of the user
        self.user_lives = 3
        self.user_score = 0
        
    def reset_game(self):
        self.screen_width = 900
        self.screen_height = 560
        self.speed = 1
        # Sealife settings = fishes the player has to avoid collecting in the net
        self.fish_speed = 2.0
        self.fish_width = 10
        self.fish_height = 10 
        # self.fish_colour = (60, 60, 60)
        self.user_speed = 7
        self.bg_colour = (135, 206, 235)
        # Plastics settings = refuse the players has to collect with the net
        self.plastic_speed = 2.0
        self.plastic_width = 10
        self.plastic_height = 10 
        # self.plastic_colour = (152, 251, 152)
        self.fish_load = 100
        print("game reset")