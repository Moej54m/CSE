class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.east = east
        self. south = south
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """

        :param new_location: The room object of which oyu are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction

        :param direction: The direction that you want to move to
        :return:The room object if it exists,or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)


# Option 2- Set all at once, modify controller
R19A = Room("Mr.Wiebe's Room")

player = Player(R19A)

playing = True

while playing:
    print(player.current_location.name)
    print(current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except keyError:
            print("I can't go that way")
        else:
            print("Command Not Found")
