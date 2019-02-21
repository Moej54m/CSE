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
        return
        self.battery -= duration * battery_loss_each_minute
        if self.battery < 0:
            self.battery = 0
            print("Your Airpods are dead. It died while you were listening to music.")
        elif self.battery == 0:
            print("Your Airpods died after the music ended.")
        else:
            print ("You have listened to all the music you want.")
            print("Your Airpod's battery is now %s" % self.battery)
            return
            battery_loss_each_minute = 3
            if self.battery <= 0:
                print("You can't use them. The battery is dead.")

    def case(self):
        print("Congratulations. Your Airpods are now protected in the case.")
        self.protection = True

    def listen_music(self, duration):
            if not self.in_range:
                print("You can't listen to music.")
                print("Your Airpods are not in range.")
                self.in_range = False

    def water_resistant(self):
        print("Oh NOOO. You dropped your Airpods in the pool. Luckily, they are water resistant.")
        self.water_resistant = True
