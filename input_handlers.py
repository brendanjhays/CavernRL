from event_queue import EventQueue
from typing import Optional
from const import Settings

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:

        key = event.sym
        if not EventQueue.queue.__contains__(key):
            EventQueue.queue.append(key)

    def ev_keyup(self, event: tcod.event.KeyUp) -> Optional[Action]:
        action: Optional[Action] = None

        if EventQueue.queue == EventQueue.secondary_queue:
            EventQueue.secondary_queue = []
            EventQueue.queue = []
            return action

        if any(EventQueue.queue.__contains__(movement_key) for movement_key in Settings.MOVEMENT_KEYS):
            action = MovementAction(dx=0, dy=0)

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
