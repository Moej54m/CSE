
class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description=(),
                                                                                                item=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.item = item


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self). __init__(name)
        self.damage = damage
        self.durability = durability


def use_weapon(self):
        self.durabilty -= 10
        print("You use the weapon and its durability drops down by 10.")


class BoneSaw(Weapon):
    def __init__(self):
        super(BoneSaw, self). __init__("Bone Saw", 20, 60)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", 20, 80)


class Sniper(Weapon):
    def __init__(self):
        super(Sniper, self). __init__("Sniper", 50, 100)


class SMG(Weapon):
    def __init__(self):
        super(SMG, self). __init__("SubMachine Gun", 15, 100)


class Rock(Weapon):
    def __init__(self):
        super(Rock, self). __init__("Rock", 5, 20)


class Spoon(Weapon):
    def __init__(self):
        super(Spoon, self). __init__("Spoon", 3, 10)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", 15, 50)


class AssaultRifle(Weapon):
    def __init__(self):
        super(AssaultRifle, self).__init__("Assault Rifle", 30, 100)

    def shoot(self):
        self.durability -= 3
        print("You fire your assault rifle. Be careful, the durability is going down every shot only for this rifle.")


class Armor(Item):  # ARMOR DEFINITION
    def __init__(self, name, defense):
        super(Armor, self). __init__(name)
        self.defense = defense


class ChestPiece(Armor):
    def __init__(self):
        super(ChestPiece, self). __init__("Chest Armor", 40)


class Gauntlets(Armor):
    def __init__(self):
        super(Gauntlets, self). __init__("Gauntlets", 20)


class Greaves(Armor):
    def __init__(self):
        super(Greaves, self). __init__("Greaves", 10)


class ShoulderPlates(Armor):
    def __init__(self):
        super(ShoulderPlates, self).__init__("Shoulder Plates", 10)


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self). __init__("Helmet", 20)


class Shield(Item):                         # SHIELD DEFINITION
    def __init__(self, name, health, durability):
        super(Shield, self).__init__(name)
        self.durability = durability
        self.health = health


class HUGESHIELD(Shield):
    def __init__(self):
        super(HUGESHIELD, self). __init__("Huge Shield", 50, 99999999999999999999)

    def drink_shield(self):
        self.durability -= 1
        self.Shield += 50


class SMALLSHIELD(Shield):
    def __init__(self):
        super(SMALLSHIELD, self). __init__("Small Shield", 25, 999999999999999999999)

    def drink_shield(self):
        self.durability -= 1
        self.Shield += 25


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor


assault_rifle = AssaultRifle()
bone_saw = BoneSaw()
sword = Sword()
sniper = Sniper()
smg = SMG()
rock = Rock()
spoon = Spoon()
knife = Knife()
chest_piece = ChestPiece()
gauntlets = Gauntlets()
greaves = Greaves()
shoulder_plates = ShoulderPlates()
helmet = Helmet()
hugeshield = HUGESHIELD()
smallshield = SMALLSHIELD()


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


LOBBY = Room('Lobby', 'FIRST_Hallway', None, 'WAITING_ROOM', 'STAIRS', None, None, " You are now in Nuketown hospital."
                                                                                   " You are inside the lobby "
                                                                                   "of the hospital."
                                                                                   " There is one the door of each of"
                                                                                   " the east, west, "
                                                                                   "and north wall.", Knife())
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
                                                                          " There is a door to the south.", [Spoon(),
                                                                                                             Helmet()])
CAFETERIA = Room('The Cafeteria', None, 'WAITING_ROOM', None, None, None, None, "You see a lot of tables. There are"
                                                                                " also many empty mini restaurants. "
                                                                                "There is a "
                                                                                "door south.", [Rock(),
                                                                                                ShoulderPlates()])
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
                                                                                                  ".", [Gauntlets(),
                                                                                                        smallshield])
Waiting_Room_2 = Room('2nd Floor Waiting Room', None, 'Laundry_Room', 'Security_Room', 'Delivery_Room', None, None,
                      "This room looks like an even"
                      "better waiting rooms with "
                      "cushioned chairs and tvs."
                      "There are doors to the east "
                      "and west.", [Greaves(), Sniper()])
Security_Room = Room('The Security Room', None, None, 'Waiting_Room_2', 'Bathroom', None, None, "This room has many "
                                                                                                "computers and some "
                                                                                                "drawers. There "
                                                                                                "are also a "
                                                                                                "few closets."
                                                                                                "There is a door west.")

Delivery_Room = Room('The Delivery Room', None, None, 'Waiting_Room_2', 'BATHROOM', None, None, "This room has a desk"
                                                                                                " with a big delivery "
                                                                                                "sign on it. There is "
                                                                                                "a door to the west.",)

BATHROOM = Room('The Bathroom', 'BALCONY', None,'Delivery_Room', None, None, None, "There are many"
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
                                                                                    "door west.", [hugeshield,
                                                                                                   AssaultRifle()])


player = Player(LOBBY)


playing = True
inventory = ['inventory', 'i']
directions = ['north', 'south', 'east', 'west', 'up', 'down']
prick_up = ['pick up', 'grab']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print("You have %s shield." % player.Shield)
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
