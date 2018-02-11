from pygame import KEYUP, KEYDOWN, K_s, K_UP, K_DOWN, K_RIGHT, K_LEFT


class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.ship = 0

    def tick(self):
        self.ship.tick()

    def render(self, canvas):
        self.ship.render(canvas)

    def load_ship(self, spaceship):
        self.ship = spaceship

    def player_key_handler(self, e):
        if e.type == KEYDOWN:
            if e.key == K_s:
                self.ship.fire = True
            if e.key == K_LEFT:
                self.ship.heading = -1
            elif e.key == K_RIGHT:
                self.ship.heading = 1
            if e.key == K_UP:
                self.ship.engine = 1
            elif e.key == K_DOWN:
                self.ship.engine = -1

        if e.type == KEYUP:
            if e.key == K_s:
                self.ship.fire = False
            if e.key == K_LEFT:
                if self.ship.heading == -1:
                    self.ship.heading = 0
            elif e.key == K_RIGHT:
                if self.ship.heading == 1:
                    self.ship.heading = 0
            if e.key == K_UP:
                if self.ship.engine == 1:
                    self.ship.engine = 0
            elif e.key == K_DOWN:
                if self.ship.engine == -1:
                    self.ship.engine = 0
