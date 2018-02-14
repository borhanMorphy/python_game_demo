from pygame import transform
from Weapon import Weapon
from gameAssets import direction_vector


# ------------ SPACESHIP CLASS ------------
#  SPACESHIP DATA FORMAT __init__:
#                   [
#       [ship center points],
#       [ship properties] (ship top speed, ship acceleration, ship agility, weapon name) with order
#                   ],
#       ship image


class Spaceship:
    def __init__(self, ship_info, ship_image):
        self.image = ship_image
        self.image_rect = ship_image.get_rect()
        self.center_points = ship_info[0]               # center x y
        self.x = ship_info[0][0] - self.image_rect[0]   # top left corner x
        self.y = ship_info[0][1] - self.image_rect[1]   # top left corner y
        self.dx = 0
        self.dy = 0
        self.properties = ship_info[1]
        self.currentSpeed = 0
        self.directionAngle = 0
        self.heading = 0            # meaning no turn just go forward
        self.engine = 0             # meaning no boost or cool command given

        self.fire = False
        self.maxAMMO = 50
        self.WEAPON = []
        for x in range(self.maxAMMO):
            self.WEAPON.append(Weapon(self.properties[3]))  # send the weapon name

    def render(self, canvas):       # render the object into the canvas
        self.draw_ship(canvas)

        for x in range(self.maxAMMO):
            if self.WEAPON[x].active:
                self.WEAPON[x].render(canvas)

    def tick(self):                 # update the values of object
        if self.heading == -1:                # turn left pressed
            self.turn_left()
        elif self.heading == 1:               # turn right pressed
            self.turn_right()

        if self.engine == 1:                  # engine boost pressed
            self.engine_boost()
        elif self.engine == -1:               # engine cool pressed
            self.engine_cool()

        if self.fire:
            self.shoot()

        self.move()

        for x in range(self.maxAMMO):
            if self.WEAPON[x].active:
                self.WEAPON[x].tick()

    def move(self):
        self.dis_calculation()
        # Update coordinates
        self.x += self.dx
        self.y += self.dy
        self.center_points[0] += self.dx
        self.center_points[1] += self.dy

    def turn_left(self):
        self.directionAngle += self.properties[2]   # agility
        if self.directionAngle >= 360:
            self.directionAngle -= 360

    def turn_right(self):
        self.directionAngle -= self.properties[2]   # agility
        if self.directionAngle < 0:
            self.directionAngle += 360

    def engine_boost(self):
        if self.currentSpeed+self.properties[1] <= self.properties[0]:    # top speed control
            self.currentSpeed += self.properties[1]
        else:
            self.currentSpeed = self.properties[0]

    def engine_cool(self):
        if self.currentSpeed-self.properties[1] >= 0:
            self.currentSpeed -= self.properties[1]
        else:
            self.currentSpeed = 0

    # calculates the displacement on x and y coordinates using direction vector
    def dis_calculation(self):
        temp_dir = self.directionAngle + 90
        if temp_dir >= 360:
            temp_dir -= 360

        self.dx = self.currentSpeed*direction_vector[temp_dir][0]
        self.dy = -self.currentSpeed*direction_vector[temp_dir][1]

    def shoot(self):
        index = self.get_shoot_index()
        if index == -1:
            return False

        temp_points = [self.center_points[0], self.center_points[1]]
        self.WEAPON[index].shoot(temp_points, self.directionAngle, self.currentSpeed)

        return True

    def get_shoot_index(self):
        for x in range(self.maxAMMO):
            if not self.WEAPON[x].active:
                return x

        return -1

    def draw_ship(self, canvas):
        rotated = transform.rotate(self.image, self.directionAngle)
        rect = rotated.get_rect()
        canvas.blit(rotated, (self.center_points[0] - rect.center[0], self.center_points[1] - rect.center[1]))

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
