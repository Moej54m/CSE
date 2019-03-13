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
        super(Sword, self).__init__("Sword", 15, 80)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", 7, 50)


class Assault_Rifle(Weapon):
    def __init__(self):
        super(Assault_Rifle, self).__init__("Assault_Rifle", 20, 100)

    def shoot(self):
        self.durabilty -= 3
        print("You fire your assault rifle.")




