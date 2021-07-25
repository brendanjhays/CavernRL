from entity import Actor
from components.ai import BaseAI, HostileEnemy
from components.fighter import Fighter

player = Actor(
    char="@",
    color=(255,255,255),
    name="Player",
    ai_cls=BaseAI,
    fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=12, defense=0, power=4),
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=18, defense=1, power=6),
)

