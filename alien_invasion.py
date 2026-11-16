
"""Python Programming
Kennedy Walker 
Starter code was given via Github
I will be modifying how the game looks and plays
Date 10/25/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship  
from bullet import Bullet


class AlienInvasion:

    def __init__(self) -> None: 
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_image = pygame.image.load(self.settings.bg_file)
        self.bg_image = pygame.transform.scale(
        self.bg_image,
        (self.settings.screen_w, self.settings.screen_h)
)

    def run_game(self) -> None:
        # Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)

            self.ship.update()
            self.bullets.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.ship.draw()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()


            pygame.display.flip() 
            self.clock.tick(self.settings.FPS)

    def _check_keydown_event(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()   
        elif event.key == pygame.K_q:
            self.running = False

    def _fire_bullet(self):
        """Create a new laser."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_event(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    pygame.quit()
    sys.exit()
