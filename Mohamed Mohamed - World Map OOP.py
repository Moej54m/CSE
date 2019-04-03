LOBBY = Room('Lobby', 'FIRST_Hallway', None, 'WAITING_ROOM', 'STAIRS', None, None, " You are now in Nuketown hospital."
                                                                                   "You are inside the lobby "
                                                                                   "of the hospital."
                                                                                   "There is one the door of each of"
                                                                                   " the east, west, "
                                                                                   "and north wall.", knife())
FIRST_HALLWAY = Room('The First Hallway', None, 'LOBBY', None, None, None, None, "You are now in the hallway of the "
                                                                                 "first"
                                                                                 " floor. There are doors that are"
                                                                                 " boarded up in the east, and west"
                                                                                 " and cannot be pried open. "
                                                                                 "The only thing you see is a"
                                                                                 " beautiful, red, hallway runner"
                                                                                 " placed on the floor. There is a"
                                                                                 " door south that appears to lead"
                                                                                 " back to the lobby.", BoneSaw())
WAITING_ROOM = Room('The Waiting Room', 'CAFETERIA', None, None, 'LOBBY', None, None, "This is the Waiting Room. "
                                                                                      "You don't"
                                                                                      " see nothing except chairs and a"
                                                                                      " table. There are doors to the"
                                                                                      " north and west.", ChestPiece())
KITCHEN = Room('The Kitchen', None, 'CAFETERIA', None, None, None, None,  "You see a lot of drawers and cabinets. "
                                                                          "There are also utensils on some tables. "
                                                                          "You see an oven and sadly a microwave."
                                                                          " There is a door to the south.", Spoon())
CAFETERIA = Room('The Cafeteria', None, 'WAITING_ROOM', None, None, None, None, "You see a lot of tables. There are"
                                                                                " also many empty mini restaurants. "
                                                                                "There is a "
                                                                                "door south.", rock(),shoulder_plates())
STAIRS = Room('Main Floor Stairs', None, None, 'Waiting_Room_2', 'Emergency_Room', None, None, "These are the stairs"
                                                                                               "for the first floor. "
                                                                                               "They appear to lead "
                                                                                               "up to the "
                                                                                               "second floor.")
EMERGENCY_HALLWAY = Room('The Emergency Hallway', None, None, 'Waiting_Room_2', None, None, None, "This appears to be"
                                                                                                  " a hallway for all "
                                                                                                  "the emergencies "
                                                                                                  "that occurred. "
                                                                                                  "There are doors to"
                                                                                                  " the south "
                                                                                                  "and the east"
                                                                                                  ".", Gauntlets())
Waiting_Room_2 = Room('2nd Floor Waiting Room', None, 'Laundry_Room', 'Security_Room', 'Delivery_Room', None, None,
                      "This room looks like an even"
                      "better waiting rooms with "
                      "cushioned chairs and tvs."
                      "There are doors to the east "
                      "and west.", Greaves(), Sniper())
Security_Room = Room('The Security Room', None, None, 'Waiting_Room_2', 'Bathroom', None, None, "This room has many "
                                                                                                "computers and some "
                                                                                                "drawers. There "
                                                                                                "are also a few closets."
                                                                                                "There is a door west.")

Delivery_Room = Room('The Delivery Room', None, None, 'Waiting_Room_2', 'BATHROOM', None, None, "This room has a desk"
                                                                                                " with a big delivery "
                                                                                                "sign on it. There is "
                                                                                                "a door to the west.",)

BATHROOM = Room('The Bathroom, 'BALCONY', None,'Delivery_Room', None, None, None, "There are many"
                                                                                  "stalls and rugs on the"
                                                                                  "ground. There are "
                                                                                  "doors to the north "
                                                                                  "and "
                                                                                  "the east.", Sword())
BALCONY = Room('The Balcony', None, 'BATHROOM', None, None, None, None, "It is finally good to get some air. "
                                                                        "Unfortunately there is nothing there.")
Laundry_Room = Room('The Laundry Room', 'Waiting_Room_2', None, 'Doctor Room', 'BACKYARD', None, None, "You see dryers "
                                                                                                       "and washers."
                                                                                                       "There are "
                                                                                                       "clothes"
                                                                                                       " in "
                                                                                                       "baskets "
                                                                                                       "everywhere. "
                                                                                                       "There is a door"
                                                                                                       " back "
                                                                                                       "north.", SMG())
BACKYARD = Room('The Backyard', None, None, 'Laundry_Room', None, None, None, "There is nothing really "
                                                                              "special about the backyard. "
                                                                              "it looks like a "
                                                                              "normal one with nice grass. "
                                                                              "There is a door to inside east.")
DOCTOR_ROOM = Room('The Doctor Room', None, None, None, 'Laundry Room', None, None, "There are a lot of computers "
                                                                                    "and telephones there. "
                                                                                    "It appears a doctor used to "
                                                                                    "stay here. "
                                                                                    "There is a "
                                                                                    "door west.", hugeshield())