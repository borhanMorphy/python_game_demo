from pygame import image  # just import image to use of image.load

# ------------- GAME ASSETS ---------------
# -- basic game variables --
canvasH = 600       # canvas height
canvasW = 800       # canvas width
gameOver = True     # game state
FPS = 30            # Frame Per Second given

# -- image formats --
PNG = '.png'
JPG = '.jpg'

# ------------------ DATA -----------------
# ------- Ship 1 -------
#   -- ship data --
ship_1_name = "VENOM"   # 'also made up , but it suits so who cares'
ship_1_info = [canvasW/2, canvasH/2,
               65, 65,
               50, 42,
               10, 0.2, 10]

ship_1_weapon_info = [0, 0,
                      15, 15,
                      15, 15,
                      20]

#   -- path descriptions --
SHIP_1_FILE_PATH = r'ship_1\\'
SHIP_1_SHOOT_FILE_PATH = r'ship_1\shoot\\'

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
        if index >= 0 & index < self.frame_count:
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


# returns as [ [ship_data], [weapon_data], ship_sprite, weapon_sprite ]
def get_ship_data(ship_name):
    data = []
    if ship_name is "VENOM":
        data.append(ship_1_info)
        data.append(ship_1_weapon_info)
        data.append(create_sprite_sheet(SHIP_1_FILE_PATH,
                                        PNG, ship_1_frame_count))

        data.append(create_sprite_sheet(SHIP_1_SHOOT_FILE_PATH,
                                        PNG, ship_1_shoot_frame_count))

    return data

# ------------------ END ------------------
