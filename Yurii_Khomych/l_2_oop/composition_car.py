class Tires:
    def __init__(self, radius=14):
        self.radius = radius


class Car:
    def __init__(self, name):
        self.name = name
        self.tires = Tires()
        # self.engine =


# Car(name="Tesla", Tires())
