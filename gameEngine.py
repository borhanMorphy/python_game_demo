from pygame import *

import gameAssets as gA

from Player import Player
from Spaceship import Spaceship

gameDisplay = None
clock = None
players = []

# -------------- MAIN FUNCTIONS ---------------


def engine_init(players_ship_name):
    init()       # initialize the module

    global gameDisplay
    gameDisplay = display.set_mode((gA.canvasW, gA.canvasH))   # set canvas dimensions

    display.set_caption('OREON')     # set game title 'i know it s made up badly'

    global clock
    clock = time.Clock()             # get clock

    players.clear()                  # 'just in case'
    i = 0                            # player id
    for p in players_ship_name:
        players.append(new_player(p, i))
        i += 1


def engine_start():
    gA.gameOver = False
    # --------------- GAME LOOP ----------------
    while not gA.gameOver:
        event_handler()

        gameDisplay.fill((0, 0, 0))  # ( R G B ) values of the background

        player_handler()             # update()

        display.update()      # update all

        clock.tick(gA.FPS)           # set fps
    # ------------------ END -------------------


def engine_terminate():
    players.clear()     # clean all players
    quit()              # terminate module

# ------------------ END -------------------


# ----------- ENGINE FUNCTIONS -------------

def event_handler():
    for e in event.get():
        if e.type == QUIT:
            gA.gameOver = True
            break
        for p in players:           # handle for all players
            p.player_key_handler(e)


def player_handler():
    for p in players:           # first tick all
        p.tick()
    for p in players:
        p.render(gameDisplay)   # after render


def new_player(player_ship_name, i):
    p = Player(str(i))                              # create player obj
    ship_data = gA.get_ship_data(player_ship_name)  # get ship data
    ship = Spaceship(ship_data[0], ship_data[1])    # create ship obj
    p.load_ship(ship)                               # load ship obj to player obj

    return p                                        # return player obj
# ------------------ END -------------------





