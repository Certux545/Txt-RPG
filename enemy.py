from items import *
class enemy:
    def __init__(self, name, health, damage, item_drop):
        self.name = name
        self.health = health
        self.damage = damage
        self.item_drop = item_drop

#enemy typ
wolf= enemy("Wolf", 10, 3, toth)
