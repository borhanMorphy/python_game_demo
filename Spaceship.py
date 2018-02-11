from math import radians, sin, cos

from Weapon import Weapon

# ------------ SPACESHIP CLASS ------------
#  SPACESHIP DATA FORMAT __init__:
#                   [
#       ship center X, ship center Y,
#       ship image width, ship image height,
#       ship real width, ship real height,
#       ship top speed, ship acceleration, ship agility
#                   ],
#       [ ship sprite sheet   ],
#       [ weapon sprite sheet ]


class Spaceship:
    def __init__(self, ship_info, ship_weapon_info,
                 ship_sprite_sheet, weapon_sprite_sheet):
        self.x = ship_info[0] - ship_info[2]/2
        self.y = ship_info[1] - ship_info[3]/2
        self.center_x = ship_info[0]
        self.center_y = ship_info[1]
        self.deltaX = 0
        self.deltaY = 0
        self.topSpeed = ship_info[6]
        self.acc = ship_info[7]
        self.shipSprite = ship_sprite_sheet
        self.ship_rW = ship_info[4]
        self.ship_rH = ship_info[5]
        self.ship_iW = ship_info[2]
        self.ship_iH = ship_info[3]
        self.currentSpeed = 0
        self.directionAngle = 90
        self.currentDirection = 0
        self.agility = ship_info[8]
        self.heading = 0            # meaning no turn just go forward
        self.engine = 0             # meaning no boost or cool command given
        self.weaponSprite = weapon_sprite_sheet
        self.fire = False
        self.WEAPON = []
        self.weapon_info = ship_weapon_info
        for x in range(100):
            self.WEAPON.append(Weapon(ship_weapon_info))

    def render(self, canvas):       # render the object into the canvas
        canvas.blit(self.shipSprite.get_image(), (self.x, self.y))

        for x in range(len(self.WEAPON)):
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
            if self.shoot() == -1:
                print("out of ammo")

        self.move()

        self.ammo_control()
        for x in range(len(self.WEAPON)):
            if self.WEAPON[x].active:
                self.WEAPON[x].tick()

    def move(self):
        self.x += self.dis_calculation_x()
        self.y += self.dis_calculation_y()
        self.center_x += self.deltaX
        self.center_y += self.deltaY

    def turn_left(self):
        if self.directionAngle+self.agility < 360:
            self.directionAngle += self.agility
        else:
            self.directionAngle += self.agility
            self.directionAngle %= 360
        self.shipSprite.animation_backward()

    def turn_right(self):
        if self.directionAngle-self.agility >= 0:
            self.directionAngle -= self.agility
        else:
            self.directionAngle -= self.agility
            self.directionAngle += 360
        self.shipSprite.animation_forward()

    def engine_boost(self):
        if self.currentSpeed+self.acc <= self.topSpeed:
            self.currentSpeed += self.acc
        else:
            self.currentSpeed = self.topSpeed

    def engine_cool(self):
        if self.currentSpeed-self.acc >= 0:
            self.currentSpeed -= self.acc
        else:
            self.currentSpeed = 0

    # calculates the displacement on x coordinate using current speed and direction
    def dis_calculation_x(self):
        self.deltaX = self.currentSpeed*cos(radians(self.directionAngle))
        return self.deltaX

    # calculates the displacement on y coordinate using current speed and direction
    def dis_calculation_y(self):
        self.deltaY = self.currentSpeed * sin(radians(self.directionAngle))
        self.deltaY *= -1
        return self.deltaY

    def shoot(self):
        index = self.get_shoot_index()
        if index == -1:
            return False

        self.weaponSprite.set_frame_index(self.shipSprite.currentframe)

        self.WEAPON[index].shoot(self.weapon_info[6], self.get_rx(0)+self.weapon_info[0],
                                 self.get_ry(0)+self.weapon_info[1],
                                 self.weaponSprite.get_image(), self.directionAngle)
        # print("ship center X = "+str(self.get_rx(0))+" bullet center X = "+str(self.get_rx(0)+self.weapon_info[0]))

        # print("ship center Y = "+str(self.get_ry(0))+" bullet center Y = "+str(self.get_ry(0)+self.weapon_info[1]))

        return True

    def get_shoot_index(self):
        for x in range(len(self.WEAPON)):
            if not self.WEAPON[x].active:
                return x

        return -1

    def ammo_control(self):
        for x in range(len(self.WEAPON)):
            if self.WEAPON[x].active:
                if self.WEAPON[x].check_collusion():     # check shoot collusion
                    self.WEAPON[x].set_default()
                    print(str(x)+" [INACTIVE]")

    def get_rx(self, shift):
        return self.x+self.ship_iW/2+shift

    def get_ry(self, shift):
        return self.y+self.ship_iH/2+shift

# ------------------ END ------------------
