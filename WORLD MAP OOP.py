class Room(object):
    def __init__(self, name, north=None, south=None, east, west, up, down):
        self.name = name
        self.north = north
        self.south =south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
LOBBY = ('Lobby', '1st_Hallway', None, 'WAITING_ROOM', 'STAIRS', None, None)
1ST_HALLWAY = ('The First Hallway', None, 'LOBBY', None, None, None, None)
WAITING_ROOM = ('The Waiting Room', 'CAFETERIA', None, None, 'LOBBY', None, None)
KITCHEN =
