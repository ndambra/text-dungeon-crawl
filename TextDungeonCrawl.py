import random

# Basic dungeon monster text based game

class Player:
    name = "Player"
    maxHitpoints = 10
    hitpoints = 10
    attack = 2
    rooms = [0,0,0,0,0,0]


    def loseHP(self,loss):
        print "%s took %d damage.\n" % (self.name, loss)
        self.hitpoints = self.hitpoints - loss

    def clearRoom(self, roomNum):
        self.rooms[roomNum-1] = 1
        print "Room cleared."

    def playerStatus(self):
        print "%s stats:\n %d HP\n %d Attack Power" % (self.name, self.hitpoints, self.attack)

    def increaseMaxHP(self, incr):
        self.maxHitpoints += incr
        self.hitpoints = self.maxHitpoints
        print "Your Max HP increases by %d" % incr
        print "HP restored.\n"
        self.playerStatus()

    def attackIncrease(self, incr):
        self.attack += incr
        print "You're Attack Power increased!"
        self.playerStatus()

    def healPlayer(self, hpUp):
        self.hitpoints += hpUp
        print "Your HP was restored by %d." % hpUp
        self.playerStatus()

class Spider:
    name = "Spider"
    hitpoints = 5
    attack = 1

    def loseHP(self,loss):
        print "The %s took %d damage.\n" % (self.name, loss)
        self.hitpoints = self.hitpoints - loss

    def monsterStatus(self):
        print "%s stats:\n %d HP\n %d Attack Power" % (self.name, self.hitpoints, self.attack)

class Skeleton:
    name = "Skeleton"
    hitpoints = 4
    attack = 1

    def loseHP(self,loss):
        print "The %s took %d damage.\n" % (self.name, loss)
        self.hitpoints = self.hitpoints - loss

    def monsterStatus(self):
        print "%s stats:\n %d HP\n %d Attack Power" % (self.name, self.hitpoints, self.attack)

class Boss:
    name = "King Kobra"
    hitpoints = 10
    attack = 2

    def loseHP(self,loss):
        print "The %s took %d damage.\n" % (self.name, loss)
        self.hitpoints = self.hitpoints - loss

    def monsterStatus(self):
        print "%s stats:\n %d HP\n %d Attack Power" % (self.name, self.hitpoints, self.attack)


def Game_Over(reason):
    switcher = {
        "start":"Wow, didn't even go in.",
        "flee":"You were not the brave soul you thought you were.\nYou flee the way you entered.",
        "dead":"You died! R.I.P"
    }
    print switcher.get(reason, "Where'd you go?")
    print "GAME OVER!!!"
    exit(0)

def Start(player):
    print "Welcome, New Player!"
    player.playerStatus()
    print "You come upon the entrance to a cave."

    notOkay = True
    while notOkay:
        choice = (raw_input("Do you enter? ")).lower()
        if choice.startswith("y") or choice.startswith("n"):
            if choice == "yes" or choice == "no":
                notOkay = False
            elif len(choice) == 1:
                notOkay = False


    if choice.startswith("y"):
        print "You enter the cave. Good luck..."
        begin = raw_input()
        room_one(player)
    else:
        Game_Over("start")

def fightStatus(player, monster):
    player.playerStatus()
    monster.monsterStatus()

def actions():
    while True:
        action = (raw_input("Do you attack or flee? ")).lower()
        if action == "attack" or action == "flee":
            return action

def attack_attack(offense, defense):
    print "The %s attacks." % offense.name
    defense.loseHP(offense.attack)

def randomMonster():
    return random.choice(['skeleton','spider'])


def room_one(player):
    if player.rooms[0] == 0:
        print "\nYou enter on the west side of a square shaped room. \nSuddenly, a spider attacks!!!"
        spider = Spider()
        attacking = True

        while attacking:
            fightStatus(player, spider)
            outcome = actions()
            if outcome == "attack":
                attack_attack(player, spider)
                if spider.hitpoints <= 0:
                    attacking = False
                else:
                    attack_attack(spider, player)
                    if player.hitpoints <= 0:
                        Game_Over("dead")
            else:
                Game_Over("flee")

        print "You've killed the spider.\n"
        player.playerStatus()
        player.clearRoom(1)
        print "There is a door to the east, a door to the south, and a door to the west."
        notOkay = True

        while notOkay:
            door = (raw_input("Which door do you take? ")).lower()
            if door == "west" or door == "south" or door == "east":
                notOkay = False
    else:
        print "\nYou enter a square shaped room."
        print "There is a dead spider in the middle."
        print "There is a door to the west, a door to the south, and a door to the east."
        notOkay = True

        while notOkay:
            door = (raw_input("Which door do you take? ")).lower()
            if door == "west" or door == "south" or door == "east":
                notOkay = False

    if door == "south":
        room_four(player)
    elif door == "east":
        room_two(player)
    else:
        print "You have exited the cave."
        Game_Over("flee")

def room_two(player):
    print "\nYou enter a square shaped room."
    if player.rooms[1] == 0:
        print "There appears to be a protective vest on a table in the center of the room."

        notOkay = True
        while notOkay:
            pickUp = (raw_input("Pick it up? ")).lower()
            if pickUp == "yes" or pickUp == "no":
                notOkay = False


        if pickUp == "yes" or pickUp == "y":
            vestStat = 2
            print "You pick up the vest."
            player.increaseMaxHP(vestStat)
            player.clearRoom(2)
            next = raw_input()
        else:
            print "You don't pick it up"
    else:
        print "\nThere is an empty table in the middle of the room"

    print "There is a door to the east, a door to the south, and a door to the west."
    notOkay = True

    while notOkay:
        door = (raw_input("Which door do you take? ")).lower()
        if door == "west" or door == "south" or door == "east":
            notOkay = False

    if door == "south":
        room_boss(player)
    elif door == "east":
        room_three(player)
    else:
        room_one(player)

def room_three(player):
    print "\nYou enter a square shaped room with a door to the west."
    if player.rooms[2] == 0:
        print "At the far end of the room there is a shiny sword propped on an altar. But....."
        print "Suddenly a skeleton attacks!"

        skeleton = Skeleton()
        attacking = True

        while attacking:
            fightStatus(player, skeleton)
            outcome = actions()
            if outcome == "attack":
                attack_attack(player, skeleton)
                if skeleton.hitpoints <= 0:
                    attacking = False
                else:
                    attack_attack(skeleton, player)
                    if player.hitpoints <= 0:
                        Game_Over("dead")
            else:
                Game_Over("flee")

        print "You've killed the skeleton."
        print "You cross the room to the alter and pick up the sword."
        player.attackIncrease(2)
        player.clearRoom(3)

        print "There is a door to the west."
        notOkay = True
        dumbCount = 0
        while notOkay:
            if dumbCount > 3:
                print "For some reason you are unable to find the only exit...."
                print "You stumble around the room for days..."
                print "You collapse from hunger and dehydration...."
                Game_Over("dead")

            door = (raw_input("Which door do you take? ")).lower()
            if door == "west":
                notOkay = False
            else:
                dumbCount += 1
                print "This isn't a tough choice....."

    else:
        print "\nYou enter a square shaped room."
        print "There is a dead skeleton in the middle and an empty alter at the far side of the room"
        print "There is a door to the west."
        notOkay = True

        while notOkay:
            door = (raw_input("Which door do you take? ")).lower()
            if door == "west":
                notOkay = False
            else:
                print "This isn't a tough choice....."

    if door == "west":
        room_two(player)

def room_four(player):
    print "\nYou enter a dark, square-shaped room."
    print "You think you see something in the dark..."
    if player.rooms[3] == 0:
        monster = randomMonster()
        if monster == "spider":
            monster = Spider()
        else:
            monster = Skeleton()
        print "\nSuddenly, a %s attacks!!!" % monster.name
        attacking = True

        while attacking:
            fightStatus(player, monster)
            outcome = actions()
            attack_attack(monster, player)
            if player.hitpoints <= 0:
                Game_Over("dead")
            else:
                if outcome == "attack":
                    attack_attack(player, monster)
                    if monster.hitpoints <= 0:
                        attacking = False
                else:
                    Game_Over("flee")

        print "You've killed the %s.\n" % monster.name
        player.playerStatus()
        player.clearRoom(4)

    else:
        print "\nIt's just a dead monster in the middle of the room."

    print "\nThere is a door to the north and south."
    notOkay = True
    while notOkay:
        door = (raw_input("Which door do you take? ")).lower()
        if door == "north" or door == "south":
            notOkay = False

    if door == "south":
        room_five(player)
    elif door == "north":
        room_one(player)
    else:
        print "You stumble around the dark room."

def room_five(player):
    print "\nYou enter a small, rectangular-shaped room."
    print "There is a small work bench in the corner of the room."
    if player.rooms[4] == 0:
        print "On the work bench is a small vial with a red liquid inside."
        print "The vial has a heart drawn on the glass."

        notOkay = True
        while notOkay:
            pickUp = (raw_input("Pick it up and drink it? ")).lower()
            if pickUp == "yes" or pickUp == "no":
                notOkay = False


        if pickUp == "yes" or pickUp == "y":
            potion = 4
            print "You pick up the vial and drink the contents."
            player.healPlayer(potion)
            player.clearRoom(5)
            next = raw_input()
        else:
            print "You don't pick it up"

    else:
        print "There is nothing on the work bench."
        print "The room is empty."

    print "There is a door to the north and east."
    notOkay = True
    while notOkay:
        door = (raw_input("Which door do you take? ")).lower()
        if door == "north" or door == "east":
            notOkay = False

    if door == "east":
        room_boss(player)
    elif door == "north":
        room_four(player)
    else:
        print "You stumble around the dark room."

def room_boss(player):
    print "\nYou enter a large, dark room."
    next = raw_input()
    print "One by one the torches on on the walls begin to light around the room."
    print "A giant, green, cobra breaks through the floor!!"
    print "##### BOSS #####"
    print "## KING KOBRA ##"
    print "################"

    boss = Boss()
    attacking = True

    while attacking:
        fightStatus(player, boss)
        outcome = actions()
        attack_attack(boss, player)
        if player.hitpoints <= 0:
            Game_Over("dead")
        else:
            if outcome == "attack":
                attack_attack(player, boss)
                if boss.hitpoints <= 0:
                    attacking = False
            else:
                print "Unable to flee!!!"

    player.clearRoom(6)
    print "\nYou've slain %s!" % boss.name
    print "\nNow that the danger has passed, you notice a large pile"
    print "of treasure on the other side of the room."
    begin = raw_input()

    if player.rooms[0] == 1 and player.rooms[2] == 1 and player.rooms[3] == 1:
        print "You collect as much treasure as you can carry"
        print "and exit the cave VICTORIOUS!"
        print "Thanks for playing!"
    else:
        print "While you are busy collecting the treasure"
        print "you don't notice a monster sneak up behind you."
        print "It got ya. You dead."
        print "Should have checked all the rooms."
        print "GAME OVER!!!"





player = Player()
Start(player)
