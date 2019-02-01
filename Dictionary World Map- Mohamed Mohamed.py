world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the north wall.",
        'PATHS': {
            'NORTH': "Parking_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A'

        }
    }
}

# Controller
play = True
current_node = world_map['R19A']
    print(current_node['NAME'])
    print(current_node[DESCRIPTION])
while playing:
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False