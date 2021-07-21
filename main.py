from event_queue import EventQueue
from typing import Set
import tcod
from const import Settings
from engine import Engine
from input_handlers import EventHandler
from event_queue import EventQueue
from dungeon_procgen import generate_dungeon
import copy
import entity_factories


def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "sampleRoguelikeGraphic.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()
    player = copy.deepcopy(entity_factories.player)
    game_map = generate_dungeon(
        max_rooms=Settings.MAX_ROOMS,
        room_min_size=Settings.ROOM_MIN_SIZE,
        room_max_size=Settings.ROOM_MAX_SIZE,
        map_width=Settings.MAP_WIDTH,
        map_height=Settings.MAP_HEIGHT,
        max_monsters_per_room=Settings.MAX_MONSTERS_PER_ROOM,
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
