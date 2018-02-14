from gameAssets import direction_vector, canvasW, canvasH, get_weapon_data
from pygame import transform

# -------------- WEAPON CLASS -------------
#  WEAPON DATA FORMAT load():
#                     [
#       [weapon shift points],
#       [bullet properties]  (speed, damage, knock back)
#                     ],
#       image


class Weapon:
    def __init__(self, weapon_name):
        self.name = weapon_name

        self.speed = 0
        self.damage = 0
        self.knock_back = 0
        self.angle = 0
        self.image = 0
        self.image_rect = 0
        self.active = False
        self.points = [0, 0]
        self.shift_points = [0, 0]
        self.center_points = [0, 0]
        self.dx = 0
        self.dy = 0
        weapon_data = get_weapon_data(weapon_name)
        self.load_weapon(weapon_data[0], weapon_data[1])

    def load_weapon(self, weapon_info, bullet_image):
        self.shift_points[0] = weapon_info[0][0]
        self.shift_points[1] = weapon_info[0][1]
        self.speed = weapon_info[1][0]
        self.damage = weapon_info[1][1]
        self.knock_back = weapon_info[1][2]
        self.image = bullet_image
        self.image_rect = bullet_image.get_rect()

    def shoot(self, points, angle, ship_speed):
        self.angle = angle
        temp_dir = self.angle + 90
        if temp_dir >= 360:
            temp_dir -= 360

        temp_shifx = (self.shift_points[0]*direction_vector[self.angle][0]) - \
                     (self.shift_points[1]*direction_vector[self.angle][1])
        temp_shify = (self.shift_points[1]*direction_vector[self.angle][0]) + \
                     (self.shift_points[0]*direction_vector[self.angle][1])

        self.center_points[0] = points[0] + temp_shifx
        self.center_points[1] = points[1] - temp_shify
        self.points[0] = self.center_points[0]
        self.points[1] = self.center_points[1]

        self.points[0] -= self.image_rect.center[0]
        self.points[1] -= self.image_rect.center[1]

        self.dx = (self.speed + ship_speed) * direction_vector[temp_dir][0]
        self.dy = -self.speed * direction_vector[temp_dir][1]

        self.active = True

    def set_defaults(self):      # call this whenever collusion occurs
        self.active = False
        self.angle = 0
        self.points = [0, 0]
        self.center_points = [0, 0]

    def render(self, canvas):
        if self.active:
            self.draw_bullet(canvas)

    def tick(self):
        if self.active:
            self.check_collusion()
            self.move()

    def move(self):
        self.points[0] += self.dx
        self.points[1] += self.dy
        self.center_points[0] += self.dx
        self.center_points[1] += self.dy

    def check_collusion(self):
        sides = [self.points[0],
                 self.points[0] + self.image_rect.size[0],
                 self.points[1],
                 self.points[1] + self.image_rect.size[1]
                 ]

        if sides[0] <= 0 or sides[1] >= canvasW or sides[2] <= 0 or sides[3] >= canvasH:
            self.set_defaults()
            #print("collusion occurred")

    def draw_bullet(self, canvas):
        rotated = transform.rotate(self.image, self.angle)
        rect = rotated.get_rect()
        canvas.blit(rotated, (self.center_points[0] - rect.center[0],
                              self.center_points[1] - rect.center[1]))

        """
        #   import py.draw to use it
        draw.rect(canvas, (255, 255, 255), (self.center_points[0] - 
                                            rect.center[0], self.center_points[1], rect.width, rect.height), 1)
        draw.line(canvas, (255, 0, 255), (self.center_points[0] - 75, self.center_points[1]), 
                  (self.center_points[0] + 75, self.center_points[1]), 1)
        draw.line(canvas, (255, 0, 255), (self.center_points[0], self.center_points[1] - 75), 
                  (self.center_points[0], self.center_points[1] + 75), 1)
        """

# ------------------ END ------------------
