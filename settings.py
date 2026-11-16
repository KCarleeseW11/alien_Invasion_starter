from pathlib import Path
class Settings:
    def __init__(self):
        self.name: str= 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images'
       
        self.image_folder = Path.cwd() / 'Assets' / 'images'

        
        self.bg_file = self.image_folder / 'background.png'

       
        self.ship_file = self.image_folder / 'ship2(no bg).png'
        self.ship_w = 80
        self.ship_h = 80

        
        self.bullet_w = 8
        self.bullet_h = 25
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 5