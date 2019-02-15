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
                       " and west and cannot be pried open.The only thing you see is a beautiful, red, hallway runner placed on the floor.",
        "There is a door south that appears to lead back to the lobby."
        'PATHS': {
            'SOUTH': 'LOBBY'

        }
    },
'WAITING_ROOM': {
        'NAME': 'The Waiting Room',
        'DESCRIPTION': "This is the Waiting Room. You don't see nothing except chairs and a table. There are doors to the north and west.",
        'PATHS':{
            'NORTH': 'CAFETERIA',
            'WEST': 'LOBBY'

        }
    },
    'KITCHEN': {
        'NAME': 'The Kitchen',
        'DESCRIPTION': "You see a lot of drawer and cabinets. There are also utensils on some tables. You see an oven and also a pantry. There is a door to the west.",
        'PATHS':{
            'SOUTH': 'CAFETERIA'

        }
    },
    'CAFETERIA': {
        'NAME': 'The Cafeteria',
        'DESCRIPTION': "You see a lot of tables. There are also many empty restaurants. As you look closer, each restaurant has a big closet.",
        'PATHS': {
            'SOUTH': 'WAITING_ROOM'

        }
    },
    'STAIRS': {
        'NAME': "Main Floor Stairs",
        'DESCRIPTION': "These are the stairs for the first floor. The appear to lead up to the second floor.",
        'PATHS': {
            'EAST': 'LOBBY'


        }
    },
    'Emergency_Hallway': {
        'NAME': "The Emergency Hallway"
        'DESCRIPTION': "This appears to be a hallway for all the emergencies that occured. There are doors to the south and the east.",
        'PATHS': {
            'EAST': 'Waiting_Room_2'

        }
    },
    'Wating_Room_2': {
        'NAME': "2nd Floor Wating Room"
        'DESCRIPTION': "This room looks like an even better waitng rooms with cushioned chairs and tvs. There are doors to the east and west.",
        'PATHS': {
            'EAST': 'Security_Room'
            'WEST': 'Delivery_Room'
            'SOUTH': 'Laundry_Room'

        }
    },
    'Security_Room': {
    'NAME': "The Security Room"
    'DESCRIPTION': " This room has many computers and some drawers. There are also a few closets. There are doors to the west. ",
    'PATHS': {
        'WEST': 'Security_Room'
        }
    },
    'Delivery_Room': {
    'NAME': "The Delivery Room"
    'DESCRIPTION': "This room has a desk with a big delivery sign on it. There is a door to the west.",
    'PATHS' {
        'WEST': 'Bathroom'
        'EAST': 'Waiting_Room_2'
        }
    },
    'BATHROOM': {
    'NAME': "The Bathroom"
    'DESCRIPTION': "There are many stalls and rugs on the ground. There are doors to the north and the east.",
    'PATHS'{
        'NORTH': 'Balcony'
        'EAST': 'Delivery_Room'
        }
    },
    'BALCONY': {
    'NAME': " The Balcony"
    'DESCRPTION': " It is finally good to get some air. Unfortunately there is nothing there.",
    'PATHS': {
        'SOUTH' 'BATHROOM'
        }
    },
    'Laundry_Room': {
    'NAME': "The Laundry Room"
    'DESCRIPTION': "You see dryers and washers. There are clothes in baskets everywhere. There is a door back north."
    'PATHS': {
        'NORTH': 'Waiting_Room_2'
        'EAST': 'Doctor Room'
        'WEST': 'BACKYARD'
        }
    },
    'BACKYARD': {
    'NAME': "The Backyard"
    'DESCRIPTION': "There is nothing really special about the backyard. it looks like a normal one with nice grass. There is a door to inside east.",
    'PATHS': {
        'EAST': 'Laundry_Room'
        }
    },
    'Doctor_Room': {
    'DESCRIPTION': "There are a lot of computers and telephones there. It appears a docotr used to stay here. There is a door west.",
    'PATHS': {
        'WEST': 'Laundry_Room'
    }
}








