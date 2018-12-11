class Car:


    def __init__(self, name="", fuel=0):

        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):

        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance