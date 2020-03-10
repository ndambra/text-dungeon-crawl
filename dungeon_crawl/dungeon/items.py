class Item(object):
    def __init__(self, item):
        self.item = item


class Vest(Item):
    def __init__(self):
        self.max_hp_incr = 2
        super().__init__('protective vest')


class Sword(Item):
    def __init__(self):
        self.attack_incr = 2
        super().__init__('shiny sword')


class Potion(Item):
    def __init__(self):
        self.hp_heal = 2
        super().__init__('healing potion')
