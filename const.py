import tcod


class Settings:
    ### Window Information ###
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    VSYNC = True
    TITLE = "AMong Us"

    ### General Information ###

    ### Map Information ###
    MAP_HEIGHT = 45
    MAP_WIDTH = 80
    ROOM_MAX_SIZE = 10
    ROOM_MIN_SIZE = 6
    MAX_ROOMS = 30
    MAX_MONSTERS_PER_ROOM = 2

    ### Controls Information ###
    UP = tcod.event.K_UP
    DOWN = tcod.event.K_DOWN
    LEFT = tcod.event.K_LEFT
    RIGHT = tcod.event.K_RIGHT
    MOVEMENT_KEYS = [UP, DOWN, LEFT, RIGHT]

class Colors:
    white = (0xFF, 0xFF, 0xFF)
    black = (0x0, 0x0, 0x0)

    player_atk = (0xE0, 0xE0, 0xE0)
    enemy_atk = (0xFF, 0xC0, 0xC0)

    player_die = (0xFF, 0x30, 0x30)
    enemy_die = (0xFF, 0xA0, 0x30)

    welcome_text = (0x20, 0xA0, 0xFF)

    bar_text = white
    bar_filled = (0x0, 0x60, 0x0)
    bar_empty = (0x40, 0x10, 0x10)
