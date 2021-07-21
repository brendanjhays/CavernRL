from event_queue import EventQueue
from typing import Set
import tcod
from const import Settings
from engine import Engine
from input_handlers import EventHandler
from event_queue import EventQueue
from entity import Entity
from dungeon_procgen import generate_dungeon


def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "sampleRoguelikeGraphic.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()
    player = Entity(int(Settings.SCREEN_WIDTH/2),
                    int(Settings.SCREEN_HEIGHT/2), "@", (255, 255, 255))
    game_map = generate_dungeon(
        max_rooms=Settings.MAX_ROOMS,
        room_min_size=Settings.ROOM_MIN_SIZE,
        room_max_size=Settings.ROOM_MAX_SIZE,
        map_width=Settings.MAP_WIDTH,
        map_height=Settings.MAP_HEIGHT,
        player=player
    )
    engine = Engine(event_handler=event_handler,
                    game_map=game_map, player=player)

    with tcod.context.new_terminal(
            Settings.SCREEN_WIDTH,
            Settings.SCREEN_HEIGHT,
            tileset=tileset,
            title=Settings.TITLE,
            vsync=Settings.VSYNC
    ) as context:
        root_console = tcod.Console(
            Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
