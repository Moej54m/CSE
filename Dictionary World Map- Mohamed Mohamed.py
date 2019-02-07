import os
world_map = {
    'LOBBY': {
        'NAME': "Lobby",
        'DESCRIPTION': " You are now in Nuketown hospital. You are inside the lobby of the hospital. There is one the",
                       " door of each of the east, west, and north wall."
        'PATHS': {
            'NORTH': '1ST_HALLWAY',
            'WEST': 'STAIRS',
            'EAST': 'WAITING_ROOM'


        }
    },
    '1ST_HALLWAY': {
        'NAME': "The First Hallway",
        'DESCRIPTION': "You are now in the hallway of the first floor. There are doors that are boarded up in the east,"
                       " and west and cannot be pried open."
                       "The only thing you see is a beautiful, red, hallway runner placed on the floor.",
        'PATHS':{
            'SOUTH': 'LOBBY'

        }
    },
    'STAIRS': {
        'NAME': "Main Floor Stairs",
        'DESCRIPTION': "These are the stairs for the first floor. The appear to lead up to the second floor.",
        'PATHS': {
            'EAST': 'LOBBY'
        }
    },
    'WAITING_ROOM': {
        'NAME': 'The Waiting Room',
        'DESCRIPTION': "This is the Waiting Room. You don't see nothing except chairs and a table.",
        'PATHS':{
            'NORTH': 'CAFETERIA',
            'WEST': 'LOBBY'
    },
    'KITCHEN': {
        'NAME': 'The Kitchen',
        'DESCRIPTION': "You see a lot of drawer and cabinets. There are also utensils on some tables. You see an oven and also a pantry.",
        'PATHS':{
            'SOUTH': 'CAFETERIA'
    },
    'CAFETERIA': {
        'NAME': 'The Cafeteria'
        'DESCRIPTION': "You see a lot of tables. There are also many empty restaurants. As you look closer, each restaurant has a big closet.",
        'PATHS':
    },









