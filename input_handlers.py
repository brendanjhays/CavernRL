from __future__ import annotations
from event_queue import EventQueue
from typing import Optional, TYPE_CHECKING
from const import Settings

import tcod.event

from actions import Action, BumpAction, EscapeAction

if TYPE_CHECKING:
    from engine import Engine


class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue
            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:

        key = event.sym

        player = self.engine.player

        if key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        if not EventQueue.queue.__contains__(key):
            EventQueue.queue.append(key)

    def ev_keyup(self, event: tcod.event.KeyUp) -> Optional[Action]:
        action: Optional[Action] = None

        player = self.engine.player

        if EventQueue.queue == EventQueue.secondary_queue:
            EventQueue.secondary_queue = []
            EventQueue.queue = []
            return action

        if any(EventQueue.queue.__contains__(movement_key) for movement_key in Settings.MOVEMENT_KEYS):
            action = BumpAction(player, dx=0, dy=0)

        if EventQueue.queue.__contains__(Settings.UP):
            action.dy -= 1
        if EventQueue.queue.__contains__(Settings.DOWN):
            action.dy += 1
        if EventQueue.queue.__contains__(Settings.LEFT):
            action.dx -= 1
        if EventQueue.queue.__contains__(Settings.RIGHT):
            action.dx += 1

        key = event.sym
        EventQueue.queue.remove(key)
        EventQueue.secondary_queue = EventQueue.queue[:]
        return action
