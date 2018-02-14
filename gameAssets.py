from pygame import image  # just import image to use of image.load
from math import sin, cos, pi

# ------------- GAME ASSETS ---------------
# -- basic game variables --
canvasW = 800           # canvas width
canvasH = 600           # canvas height
canvasW_H = canvasW/2   # canvas width / 2
canvasH_H = canvasH/2   # canvas height / 2
gameOver = True         # game state
FPS = 30                # Frame Per Second given

# -- direction vector --
D2R = (pi * 2) / 360
direction_vector = list([[cos(D2R*degrees), sin(D2R*degrees)] for degrees in range(360)])
direction_vector[0][1] = 0
direction_vector[90][0] = 0
direction_vector[180][1] = 0
direction_vector[270][0] = 0

# ------------------ DATA -----------------
# ------- Ship 1 -------
#   -- ship data --
ship_1_name = "VENOM"   # 'also made up , but it suits so who cares'
ship_1_info = [
        [canvasW/2, canvasH/2],
        [10, 0.2, 5, 'REGULAR']
              ]

#   -- weapon data --
weapon_1_info = [
        [0, 10],
        [20, 10, 5]
                ]

#   -- path descriptions --
SHIP_1_FILE_PATH = r'ship6.png'
WEAPON_1_FILE_PATH = r'bullet1.png'

#   -- sprite sheet frame counts --
ship_1_frame_count = 36
ship_1_shoot_frame_count = 36
# -----------------------


# ------------------ END ------------------

# ---------- SPRITE SHEET CLASS -----------
# to handle animations using frame by frame logic


class SpriteSheet:
    def __init__(self, frame_count, frames, current_frame):
        self.frame_count = frame_count      # total frames
        self.frames = frames                # image array
        self.currentframe = current_frame   # shown frame index

    def animation_forward(self):            # go forward indexes
        if self.currentframe == self.frame_count-1:
            self.currentframe = 0
        else:
            self.currentframe += 1

    def animation_backward(self):           # go backward indexes
        if self.currentframe == 0:
            self.currentframe = self.frame_count - 1
        else:
            self.currentframe -= 1

    def get_image(self):                    # return current frame shown
        return self.frames[self.currentframe]

    def set_frame_index(self, index):       # set any frame as current_frame
        if index >= 0 and index < self.frame_count:
            self.currentframe = index

# ------------------ END ------------------

# ------------ USEFUL FUNCTIONS -----------


def create_sprite_sheet(path, image_format, count):
    i = 0
    frames = []
    while i != count:
        temp_path = path + str(i) + image_format
        temp_image = image.load(temp_path)
        frames.append(temp_image)
        i += 1

    return SpriteSheet(len(frames), frames, 0)


# returns as [ [ship_data], image]
def get_ship_data(ship_name):
    data = []
    if ship_name is "VENOM":
        data.append(ship_1_info)
        data.append(image.load(SHIP_1_FILE_PATH))

    return data


# returns as [ [weapon_data], image]
def get_weapon_data(weapon_name):
    data = []
    if weapon_name is 'REGULAR':
        data.append(weapon_1_info)
        data.append(image.load(WEAPON_1_FILE_PATH))

    return data

# ------------------ END ------------------
