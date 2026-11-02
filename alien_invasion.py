"""Python Programming
Kennedy Walker 
Starter code was giving via Github
I will be modifying how the game looks and plays
Date 10/25/2026
"""
import sys
import pygame
from settings import Settings

class AlienInvasion:

    def __init__(self) -> none:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption(self.settings.name)

    
        self.running = True
        self.clock = pygame.time.Clock()
        running = True
    def run_game (self) -> None:
        #Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                     self._check_keydown_event(event)
                 

    def _check_keydown_event(self, event) -> None:
            pass
    def _check_keydown_event(self, event) -> None:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_RIGHT:
                self.event.ship.moving_left = True
            elif event.key == pygame.K_q:
                self.running = False
                pygame.quit()
                sys.exit
        

                
                
            

                pygame.display.flip()
                self.clock.tick(60)



if __name__ == '__main__':
    pass


#adding background
BASE_DIR = Path(__file__).resolve().parent
bg_path = BASE_DIR / "image" / "Starbasesnow.png"