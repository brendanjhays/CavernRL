from typing import Set
import tcod
from const import Settings, Colors
from engine import Engine
from dungeon_procgen import generate_dungeon
import copy
import entity_factories
import traceback


def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "sampleRoguelikeGraphic.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)
    engine.game_map = generate_dungeon(
        max_rooms=Settings.MAX_ROOMS,
        room_min_size=Settings.ROOM_MIN_SIZE,
        room_max_size=Settings.ROOM_MAX_SIZE,
        map_width=Settings.MAP_WIDTH,
        map_height=Settings.MAP_HEIGHT,
        max_monsters_per_room=Settings.MAX_MONSTERS_PER_ROOM,
        engine=engine
    )
    engine.update_fov()

    engine.message_log.add_message(
        "You wake up in a musty cave, with all of your belongings gone", Colors.welcome_text
    )

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
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:
                traceback.print_exc()
                engine.message_log.add_message(
                    traceback.format_exc(), Colors.error)


if __name__ == "__main__":
    main()
