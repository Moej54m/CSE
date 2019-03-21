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
        super(BoneSaw, self). __init__("Sword", 20, 60)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", 20, 80)


class Sniper(Weapon):
    def __init__(self):
        super(Sniper, self). __init__("Sword", 50, 100)


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
        self.shield += 50


class SMALLSHIELD(Shield):
    def __init__(self):
        super(SMALLSHIELD, self). __init__("Huge Shield", 25, 999999999999999999999)

    def drink_shield(self):
        self.durability -= 1
        self.shield += 25


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.Armor = Armor
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon

    def receive_damage(self, damage: int):
        if self.Armor > damage:
            print(" No damage is done because of the armor.")
        elif self.shield <= 0:
            print("%s enemy died" % self.name)
            return
        else:
            self.shield -= damage - self.Armor
            print("%s has %d shield remaining." % (self.name, self.shield))

    def attack(self, enemy):
        print("%s attacks %s for %d damage." % (self.name, enemy.name, self.weapon))
        enemy.receive_damage(self.damage)

