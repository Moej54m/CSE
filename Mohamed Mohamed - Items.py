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


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", 20, 80)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", 15, 50)


class AssaultRifle(Weapon):
    def __init__(self):
        super(AssaultRifle, self).__init__("Assault Rifle", 30, 100)

    def shoot(self):
        self.durability -= 3
        print("You fire your assault rifle. Be careful, the durability is going down ever shot.")


class Armor(Item):
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
class Helemet(Armor):
    def __init__(self):
        super(Greaves, self). __init__("Helmet", 20)











