class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name: object, damage: object, durability: object) -> object:
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
        super(SMALLSHIELD, self). __init__("Huge Shield", 25, 999999999999999999999)

    def drink_shield(self):
        self.durability -= 1
        self.shield += 25


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.defense > damage:
            print("No damage is done because of some extravagant armor.")
        else:
            self.health -= damage - self.armor.defense
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
Sword = Weapon("Sword", 30, 100)
SMG = Weapon("SubMachineGun", 15, 100)
ChestPiece = Armor("Chest Armor", 40)

# Characters
Zombie = Character("Zombie", 100, Sword, Armor("Generic Armor", 2))
Ghost = Character("Ghost", 10000, SMG, ChestPiece)

Zombie.attack(Ghost)
Ghost.attack(Zombie)
Ghost.attack(Zombie)
Ghost.attack(Zombie)
