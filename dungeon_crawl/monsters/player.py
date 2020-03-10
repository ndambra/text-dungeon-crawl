from dungeon_crawl.monsters.monster import Monster


class Player(Monster):
    def __init__(self, name):
        super().__init__(name, 10, 2)
        self.max_hitpoints = 10
        self.rooms = [0, 0, 0, 0, 0, 0]

    def clear_room(self, room_num, mob):
        self.get_status()
        self.rooms[room_num-1] = 1
        print("You killed the {}.".format(mob.name))
        print("Room cleared.")

    def increase_max_hp(self, incr):
        self.max_hitpoints += incr
        self.hitpoints = self.maxHitpoints
        print("Your Max HP increases by {}".format(incr))
        print("HP restored.\n")
        self.status()

    def attack_increase(self, incr):
        self.attack += incr
        print("You're Attack Power increased!")
        self.status()

    def heal_player(self, hp_up):
        self.hitpoints += hp_up
        print("Your HP was restored by {}.".format(hp_up))
        self.status()
