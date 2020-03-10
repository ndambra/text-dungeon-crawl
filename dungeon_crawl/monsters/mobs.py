from dungeon_crawl.monsters.monster import Monster


class Spider(Monster):
    def __init__(self):
        super().__init__("Spider", 5, 1)


class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 4, 1)


class Boss(Monster):
    def __init__(self):
        super().__init__("King Kobra", 10, 2)
