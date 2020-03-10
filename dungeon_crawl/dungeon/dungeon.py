import random
from dungeon_crawl.dungeon.room import Room
from dungeon_crawl.monsters.mobs import *
from dungeon_crawl.dungeon.items import *
import dungeon_crawl.dungeon.actions as action


def random_mob():
    monster = random.choice(['skeleton', 'spider'])
    if monster == "spider":
        return Spider()
    else:
        return Skeleton()


items = {
    'vest': Vest(),
    'sword': Sword(),
    'potion': Potion(),
    'treasure': Item('treasure')
}

mobs = {
    'spider': Spider(),
    'skeleton': Skeleton(),
    'boss': Boss(),
    'random': random_mob()
}


def explore(player, room):
    print(room.enter_text)

    if player.rooms[room.room-1] == 0:
        if room.mob is not None:
            action.fight(player, room.mob)
            player.clear_room(room.room, room.mob)

        if room.items is not None:
            print("This room has an item: {}".format(room.items.item))

    choice = action.get_input(room.prompt, room.options)

    if room.exits[choice] == 0:
        print("Game ending from room: {}".format(room.room))
        if room.room == 0:
            action.game_over('start')
        else:
            action.game_over('flee')
    else:
        next_room = room.exits[choice]
        explore(player, next_room)


# def room_one(player):
#     if player.rooms[0] == 0:
#
#
#         while attacking:
#             action.fightStatus(player, spider)
#             outcome = actions()
#             if outcome == "attack":
#                 attack_attack(player, spider)
#                 if spider.hitpoints <= 0:
#                     attacking = False
#                 else:
#                     attack_attack(spider, player)
#                     if player.hitpoints <= 0:
#                         Game_Over("dead")
#                 # end else
#             else:
#                 Game_Over("flee")
#             # end else
#         # end while loop
#
#         print("You've killed the spider.\n")
#         player.playerStatus()
#         player.clearRoom(1)
#         # exit directions
#         notOkay = True
#
#         while notOkay:
#             door = input("Which door do you take? ").lower()
#             if door == "west" or door == "south" or door == "east":
#                 notOkay = False
#             # end if
#         # end while loop
#     else:
#         print("\nYou enter a square shaped room.")
#         print("There is a dead spider in the middle.")
#         print("There is a door to the west, a door to the south, and a door to the east.")
#         notOkay = True
#
#         while notOkay:
#             door = input("Which door do you take? ").lower()
#             if door == "west" or door == "south" or door == "east":
#                 notOkay = False
#             # end if
#         # end while loop
#     # end else
#
#     if door == "south":
#         room_four(player)
#     elif door == "east":
#         room_two(player)
#     else:
#         print("You have exited the cave.")
#         Game_Over("flee")
#     # end else
#
# def room_two(player):
#     print("\nYou enter a square shaped room.")
#     if player.rooms[1] == 0:
#         print("There appears to be a protective vest on a table in the center of the room.")
#
#         notOkay = True
#         while notOkay:
#             pickUp = input("Pick it up? ").lower()
#             if pickUp == "yes" or pickUp == "no":
#                 notOkay = False
#             # end if
#         # end while loop
#
#         if pickUp == "yes" or pickUp == "y":
#             vestStat = 2
#             print("You pick up the vest.")
#             player.increaseMaxHP(vestStat)
#             player.clearRoom(2)
#             next = input()
#         else:
#             print("You don't pick it up")
#         # end else
#     else:
#         print("\nThere is an empty table in the middle of the room")
#     # end else
#
#     print("There is a door to the east, a door to the south, and a door to the west.")
#     notOkay = True
#
#     while notOkay:
#         door = input("Which door do you take? ").lower()
#         if door == "west" or door == "south" or door == "east":
#             notOkay = False
#         # end if
#     # end while loop
#
#     if door == "south":
#         room_boss(player)
#     elif door == "east":
#         room_three(player)
#     else:
#         room_one(player)
#     # end else
#
# def room_three(player):
#     print("\nYou enter a square shaped room with a door to the west.")
#     if player.rooms[2] == 0:
#         print("At the far end of the room there is a shiny sword propped on an altar. But.....")
#         print("Suddenly a skeleton attacks!")
#
#         skeleton = Skeleton()
#         attacking = True
#
#         while attacking:
#             fightStatus(player, skeleton)
#             outcome = actions()
#             if outcome == "attack":
#                 attack_attack(player, skeleton)
#                 if skeleton.hitpoints <= 0:
#                     attacking = False
#                 else:
#                     attack_attack(skeleton, player)
#                     if player.hitpoints <= 0:
#                         Game_Over("dead")
#                     # end if
#                 # end else
#             else:
#                 Game_Over("flee")
#             # end else
#         # end while loop
#
#         print("You've killed the skeleton.")
#         print("You cross the room to the alter and pick up the sword.")
#         player.attackIncrease(2)
#         player.clearRoom(3)
#     else:
#         print("\nYou enter a square shaped room.")
#         print("There is a dead skeleton in the middle and an empty alter at the far side of the room")
#     # end else
#
#     print("There is a door to the west.")
#     notOkay = True
#     dumbCount = 0
#     while notOkay:
#         if dumbCount > 3:
#             print("For some reason you are unable to find the only exit....")
#             print("You stumble around the room for days...")
#             print("You collapse from hunger and dehydration....")
#             Game_Over("dead")
#         # end if
#
#         door = input("Which door do you take? ").lower()
#         if door == "west":
#             notOkay = False
#         else:
#             dumbCount += 1
#             print("This isn't a tough choice.....")
#         # end else
#     # end while
#
#     if door == "west":
#         room_two(player)
#
# def room_four(player):
#     print("\nYou enter a dark, square-shaped room.")
#     print("You think you see something in the dark...")
#     if player.rooms[3] == 0:
#         monster = randomMonster()
#         if monster == "spider":
#             monster = Spider()
#         else:
#             monster = Skeleton()
#         # end else
#         print("\nSuddenly, a {} attacks!!!".format(monster.name))
#         attacking = True
#
#         while attacking:
#             fightStatus(player, monster)
#             outcome = actions()
#             attack_attack(monster, player)
#             if player.hitpoints <= 0:
#                 Game_Over("dead")
#             else:
#                 if outcome == "attack":
#                     attack_attack(player, monster)
#                     if monster.hitpoints <= 0:
#                         attacking = False
#                     # end if
#                 else:
#                     Game_Over("flee")
#                 # end else
#             # end else
#         # end whie loop
#
#         print("You've killed the {}.\n".format(monster.name))
#         player.playerStatus()
#         player.clearRoom(4)
#     else:
#         print("\nIt's just a dead monster in the middle of the room.")
#     # end else
#
#     print("\nThere is a door to the north and south.")
#     notOkay = True
#     while notOkay:
#         door = input("Which door do you take? ").lower()
#         if door == "north" or door == "south":
#             notOkay = False
#         # end if
#     # end while
#
#     if door == "south":
#         room_five(player)
#     elif door == "north":
#         room_one(player)
#     else:
#         print("You stumble around the dark room.")
#     # end else
#
# def room_five(player):
#     print("\nYou enter a small, rectangular-shaped room.")
#     print("There is a small work bench in the corner of the room.")
#     if player.rooms[4] == 0:
#         print("On the work bench is a small vial with a red liquid inside.")
#         print("The vial has a heart drawn on the glass.")
#
#         notOkay = True
#         while notOkay:
#             pickUp = input("Pick it up and drink it? ").lower()
#             if pickUp == "yes" or pickUp == "no":
#                 notOkay = False
#             # end if
#         # end while loop
#
#         if pickUp == "yes" or pickUp == "y":
#             potion = 4
#             print("You pick up the vial and drink the contents.")
#             player.healPlayer(potion)
#             player.clearRoom(5)
#             next = input()
#         else:
#             print("You don't pick up the potion.")
#         # end else
#     else:
#         print("There is nothing on the work bench.")
#         print("The room is empty.")
#     # end else
#
#     print("There is a door to the north and east.")
#     notOkay = True
#     while notOkay:
#         door = input("Which door do you take? ").lower()
#         if door == "north" or door == "east":
#             notOkay = False
#         # end if
#     # end while loop
#
#     if door == "east":
#         room_boss(player)
#     elif door == "north":
#         room_four(player)
#     else:
#         print("You stumble around the dark room.")
#     # end else
#
# def room_boss(player):
#     print("\nYou enter a large, dark room.")
#     next = input()
#     print("One by one the torches on on the walls begin to light around the room.")
#     print("A giant, green, cobra breaks through the floor!!")
#     print("##### BOSS #####")
#     print("## KING KOBRA ##") # probably shouldn't hard code this
#     print("################")
#
#     boss = Boss()
#     attacking = True
#
#     while attacking:
#         fightStatus(player, boss)
#         outcome = actions()
#         attack_attack(boss, player)
#         if player.hitpoints <= 0:
#             Game_Over("dead")
#         else:
#             if outcome == "attack":
#                 attack_attack(player, boss)
#                 if boss.hitpoints <= 0:
#                     attacking = False
#                 # end if
#             else:
#                 print("Unable to flee!!!")
#             # end else
#         # end else
#     # end while loop
#
#     player.clearRoom(6)
#     print("\nYou've slain {}!".format(boss.name))
#     print("\nNow that the danger has passed, you notice a large pile")
#     print("of treasure on the other side of the room.")
#     begin = input()
#
#     if player.rooms[0] == 1 and player.rooms[2] == 1 and player.rooms[3] == 1:
#         print("You collect as much treasure as you can carry")
#         print("and exit the cave VICTORIOUS!")
#         print("Thanks for playing!")
#     else:
#         print("While you are busy collecting the treasure")
#         print("you don't notice a monster sneak up behind you.")
#         print("It got ya. You dead.")
#         print("Should have checked all the rooms.")
#         print("GAME OVER!!!")
#     # end else

entrance = Room(0, None, None)
room_one = Room(1, None, mobs['spider'])
room_two = Room(2, items['vest'], None)
room_three = Room(3, items['sword'], mobs['skeleton'])
room_four = Room(4, None, mobs['random'])
room_five = Room(5, items['potion'], None)
room_boss = Room('boss', None, mobs['boss'])


def setup_dungeon():
    entrance.add_exits({'yes': room_one, 'y': room_one, 'n': 0, 'no': 0})
    entrance.set_enter_text("You come upon the entrance to a cave.")
    entrance.set_prompt("Do you enter? ")

    room_one.add_exits({'east': room_two, 'south': room_four, 'west': 0})
    room_one.set_enter_text(("You enter a square shaped room.\nThere is a door to the east, "
                             "a door to the south, and a door to the west."
                             "\nSuddenly, a spider attacks!!!"))

    room_two.add_exits({'south': room_boss, 'east': room_three, 'west': room_one})
    room_two.set_enter_text(("\nYou enter a another  square shaped room.\nThere is a door to the east, "
                             "a door to the south, and a door to the west.\nThere appears to "
                             "be a protective vest on a table in the center of the room."))

    room_three.add_exits({'west': room_two})
    room_three.set_enter_text(("\nYou enter another square shaped room with a door to the west.\nAt the "
                               "far end of the room there is a shiny sword propped on an altar. But....."
                               "\nSuddenly a skeleton attacks!"))

    room_four.add_exits({'north': room_one, 'south': room_five})
    room_four.set_enter_text("\nYou enter a dark, square-shaped room. There is a door to the north and south."
                             "\nYou think you see something in the dark...\nSuddenly, a monster attacks!!!")

    room_five.add_exits({'north': room_four, 'east': room_boss})
    room_five.set_enter_text("\nYou enter a small, rectangular-shaped room. There is a door to the north and east."
                             "\nThere is a small work bench in the corner of the room. On the work bench is a small "
                             "\nvial with a red liquid inside. The vial has a heart drawn on the glass. ")

    room_boss.set_enter_text("\nYou enter a large, dark room.\nOne by one the torches on on the walls begin to light "
                             "around the room.\nOne by one the torches on on the walls begin to light around the room."
                             "\nA giant, green, cobra breaks through the floor!!\n##### BOSS #####\n## KING KOBRA ## "
                             "\n################")
    room_boss.set_prompt("")

    return entrance


start_point = setup_dungeon()