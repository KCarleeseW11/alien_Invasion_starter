
"""Python Programming
Kennedy Walker 
Starter code was given via Github
I will be modifying how the game looks and plays
Date 10/25/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship  # FIX: added Ship import


class AlienInvasion:

    def __init__(self) -> None:  # FIX: corrected None
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

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
            self.screen.fill((0, 0, 0))
            self.ship.draw()

            pygame.display.flip()  # FIX: corrected indentation
            self.clock.tick(self.settings.FPS)

    def _check_keydown_event(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # FIX: self.ship, not self.event.ship
        elif event.key == pygame.K_q:
            self.running = False

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
