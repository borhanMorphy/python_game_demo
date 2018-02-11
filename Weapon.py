from math import cos, sin, radians
from gameAssets import canvasH, canvasW


# -------------- WEAPON CLASS -------------
#  WEAPON DATA FORMAT __init__:
#                     [
#       weapon center X, weapon center Y,
#       bullet image width, bullet image height
#       bullet real width, bullet real height,
#       bullet speed
#                     ]


class Weapon:
    def __init__(self, weapon_data):
        self.speed = 0
        self.bullet_angle = 0
        self.bullet_imageW = weapon_data[0]
        self.bullet_imageH = weapon_data[1]
        self.bullet_realW = weapon_data[2]
        self.bullet_realH = weapon_data[3]
        self.bullet_image = 0
        self.active = False
        self.x = 0
        self.y = 0
        self.disX = 0
        self.disY = 0

    def shoot(self, speed, start_x, start_y, image, angle):
        self.x = start_x-self.bullet_imageW/2
        self.y = start_y-self.bullet_imageH/2
        self.speed = speed
        self.disX = self.speed*cos(radians(angle))
        self.disY = -1*self.speed*sin(radians(angle))
        self.bullet_image = image
        self.active = True

    def set_default(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.disX = 0
        self.disY = 0
        self.bullet_image = 0
        self.active = False

    def render(self, canvas):
        canvas.blit(self.bullet_image, (self.x, self.y))

    def tick(self):
        self.move()

    def move(self):
        self.x += self.disX
        self.y += self.disY

    def check_collusion(self):
        if self.get_rx(-self.bullet_realW/2) <= 0 \
                or self.get_rx(self.bullet_realW/2) >= canvasW \
                or self.get_ry(-self.bullet_realH/2) <= 0 \
                or self.get_ry(self.bullet_realH/2) >= canvasH:
            print("collusion occurred")
            return True
        return False

    def get_rx(self, shift):
        return self.x+(self.bullet_imageW/2)+shift

    def get_ry(self, shift):
        return self.y+(self.bullet_imageH/2)+shift

# ------------------ END ------------------
