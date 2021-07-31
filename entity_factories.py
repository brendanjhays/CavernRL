from entity import Actor, Item
from components.ai import BaseAI, HostileEnemy
from components.fighter import Fighter
from components.consumable import Consumable, HealingConsumable

player = Actor(
    char="@",
    color=(255,255,255),
    name="Player",
    ai_cls=BaseAI,
    fighter=Fighter(hp=30, defense=2, power=5, regeneration=1),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=12, defense=0, power=4, regeneration=0),
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=18, defense=1, power=5, regeneration=0),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4)
)

