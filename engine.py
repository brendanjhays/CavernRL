from __future__ import annotations

from numpy import maximum
from render_functions import render_bar, render_names_at_mouse
from message_log import MessageLog
from typing import TYPE_CHECKING
from tcod.console import Console
from tcod.map import compute_fov
from input_handlers import MainGameEventHandler

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap
    from input_handlers import EventHandler


class Engine:

    game_map: GameMap

    def __init__(self, player: Actor):
        self.event_handler: EventHandler = MainGameEventHandler(self)
        self.player = player
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)

    def update_tick(self) -> None:
        self.handle_enemy_turns()
        for entity in self.game_map.actors:
            entity.fighter.hp += entity.fighter.regeneration
        pass

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.actors:
            if entity.ai and entity != self.player:
                entity.ai.perform()

    def update_fov(self) -> None:
        """Recompute visible area based on the player"""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:
        self.game_map.render(console)
        self.message_log.render(console=console, x=21, y=45, width=40, height=5)

        render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )

        render_names_at_mouse(console=console, x=21, y=44, engine=self)
