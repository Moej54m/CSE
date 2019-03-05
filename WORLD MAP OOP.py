class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description=()):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
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
        return globals()[name_of_room]


LOBBY = Room('Lobby', 'FIRST_Hallway', None, 'WAITING_ROOM', 'STAIRS', None, None, " You are now in Nuketown hospital. "
                                                                                   "You are inside the lobby "
                                                                                   "of the hospital."
                                                                                   "There is one the door of each of"
                                                                                   " the east, west, and north wall.")
FIRST_HALLWAY = Room('The First Hallway', None, 'LOBBY', None, None, None, None, "You are now in the hallway of the "
                                                                                 "first"
                                                                                 " floor. There are doors that are"
                                                                                 " boarded up in the east, and west"
                                                                                 " and cannot be pried open. "
                                                                                 "The only thing you see is a"
                                                                                 " beautiful, red, hallway runner"
                                                                                 " placed on the floor. There is a"
                                                                                 " door south that appears to lead"
                                                                                 " back to the lobby.")
WAITING_ROOM = Room('The Waiting Room', 'CAFETERIA', None, None, 'LOBBY', None, None, "This is the Waiting Room. "
                                                                                      "You don't"
                                                                                      " see nothing except chairs and a"
                                                                                      " table. There are doors to the"
                                                                                      " north and west.")
KITCHEN = Room('The Kitchen', None, 'CAFETERIA', None, None, None, None,  "You see a lot of drawers and cabinets. "
                                                                          "There are also utensils on some tables. "
                                                                          "You see an oven and sadly a microwave."
                                                                          " There is a door to the south.")
CAFETERIA = Room('The Cafeteria', None, 'WAITING_ROOM', None, None, None, None, "You see a lot of tables. There are"
                                                                                " also many empty mini restaurants. "
                                                                                "There is a door south.")
STAIRS = ('Main Floor Stairs', None, None, 'Waiting_Room_2', 'Emergency_Room', None)
player = Player(LOBBY)


playing = True
directions = ['north', 'east', 'south', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
        else:
            print("Command Not Found")
