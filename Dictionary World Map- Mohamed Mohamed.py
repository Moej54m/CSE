world map = {
    'Nuketown Hospital': {
        'NAME': "Lobby",
        'DESCRIPTION': " You are now in Nuketown hospital. You are inside the lobby of the hospital. There is one the",
                       " door of each of the east, west, and north wall."
        'PATHS': {
            'NORTH': '1st_Hallway',
            'WEST': 'Stairs',
            'EAST': 'Waiting_Room'


        }
    },
    '1st_Hallway': {
        'NAME': "The First Hallway",
        'DESCRIPTION': "You are now in the hallway of the first floor. There are doors that are boarded up in the east",
                       " and west and cannot be pried open."
                       "The only thing you see is a beautiful, red, hallway runner placed on the floor."
        'PATHS':{
            'SOUTH': 'Lobby'

        }
    },
    'Stairs': {
        'NAME': "Main Floor Stairs",
        'DESCRIPTION': "These are the stairs for the first floor. The appear to lead up to the second floor."
        'PATHS': {
            'EAST': 'Lobby'
        }
}












