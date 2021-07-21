import tcod


class Settings:
    ### Window Information ###
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    VSYNC = True
    TITLE = "I'm too lazy to come up with a title"

    ### General Information ###

    ### Map Information ###
    MAP_HEIGHT = 45
    MAP_WIDTH = 80
    ROOM_MAX_SIZE = 10
    ROOM_MIN_SIZE = 6
    MAX_ROOMS = 30

    ### Controls Information ###
    UP = tcod.event.K_UP
    DOWN = tcod.event.K_DOWN
    LEFT = tcod.event.K_LEFT
    RIGHT = tcod.event.K_RIGHT
    MOVEMENT_KEYS = [UP, DOWN, LEFT, RIGHT]
