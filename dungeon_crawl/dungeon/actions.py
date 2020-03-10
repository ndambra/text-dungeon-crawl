def game_over(reason):
    switcher = {
        'start': "Wow, didn't even go in.",
        'flee': "You were not the brave soul you thought you were.\nYou flee the way you entered.",
        'dead': "You died! R.I.P"
    }
    print(switcher.get(reason, "Where'd you go?"))
    print("GAME OVER!!!")
    exit(0)


def get_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options or choice == 'quit':
            return choice
        # end condition
    # end while loop


def fight_status(player, mob):
    player.get_status()
    mob.get_status()


def attack_attack(offense, defense):
    print("{} attacks.".format(offense.name))
    defense.lose_hp(offense.attack)


def fight(player, mob):
    prompt = "What do you do? "
    options = ['attack', 'flee', 'help']
    fighting = True

    while fighting:
        fight_status(player, mob)
        action = get_input(prompt, options)
        if action == "attack":
            attack_attack(player, mob)
            if mob.hitpoints <= 0:
                fighting = False
            else:
                attack_attack(mob, player)
                if player.hitpoints <= 0:
                    game_over("dead")
        elif action == "flee" or action == "quit":
            game_over("flee")
        elif action == "stat":
            fight_status(player, mob)
        else:
            print("I don't understand.\n")


def grab_item():
    pass
