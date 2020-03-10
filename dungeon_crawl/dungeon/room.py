class Room(object):
    def __init__(self, room, items, mob):
        self.room = room
        self.exits = {} # direction of doors in the room and what rooms they lead to
        self.items = items
        self.mob = mob
        self.enter_text = ''
        self.prompt = 'Which door do you take? '
        self.options = []

    def display_room(self):
        pass

    def fight(self):
        pass

    def navigate(self):
        pass

    def collect_item(self):
        pass

    # prompts are the questions asked to the user to get input
    def set_prompt(self, prompt):
        self.prompt = prompt

    # options are the only choices the user can enter
    def add_options(self, options):
        self.options = options

    # the text that describes the scen upon entering a room
    def set_enter_text(self, text):
        self.enter_text = text

    # the doors of each room, and the direction they are in
    def add_exits(self, exits):
        self.exits = exits
        for direction in exits:
            self.options.append(direction)
