class Monster(object):

    def __init__(self, name, hp, att):
        self.name = name
        self.hitpoints = hp
        self.attack = att

    def lose_hp(self, loss):
        print("{} took {} damage.\n".format(self.name, loss))
        self.hitpoints = self.hitpoints - loss

    def get_status(self):
        return "{}'s stats:\n{} HP\n{} Attack Power".format(self.name, self.hitpoints, self.attack)
