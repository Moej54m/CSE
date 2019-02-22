class Airpods(object):
    def __init__(self):
        self.protection = True
        self.battery = charge_left
        self.in_range = True
        self.water_resistant = True
        self.case = True

    def charge(self, time):
        self.battery += time
        if self.battery > 50:
            self.battery = 50

    def case(self):
        print("Congratulations. Your Airpods are now protected in the case.")
        self.protection = True

    def listen_music(self):
        if not self.in_range:
            print("You can't listen to music.")
            print("Your Airpods are not in range.")
            self.in_range = False

    def water_resistant(self):
        print("Oh NOOO. You dropped your Airpods in the pool. Luckily, they are water resistant.")
        self.water_resistant = True
