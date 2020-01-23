class Car:
    _car_hood_opening = 0
    __software_version = 1

    def __init__(self):
        self.__tires_diameter = 15

    def drive(self):
        print("driving")

    def _open_car_hood(self):
        self._car_hood_opening += 1
        if self._car_hood_opening >= 2:
            print(
                "You should go to the service or update your software manually"
            )

    def get_tires_diameter(self):
        print(f"Car tires diameter is {self.__tires_diameter}")
        return self.__tires_diameter

    def set_tires_diameter(self, diameter):
        self.__tires_diameter = diameter
        print(
            f"Successfully install custom tires diameter "
            f"{self.__tires_diameter}"
        )

    def del_tires_diameter(self):
        print("We've set default diameter for your tires")
        self.__tires_diameter = 15

    tires_diameter = property(
        fget=get_tires_diameter,
        fset=set_tires_diameter,
        fdel=del_tires_diameter,
        doc="Tires diameter property",
    )


tesla_car = Car()
tesla_car.drive()
tesla_car._open_car_hood()
tesla_car.drive()
tesla_car._open_car_hood()


tesla_car.tires_diameter
tesla_car.tires_diameter = 21
del tesla_car.tires_diameter
tesla_car.tires_diameter
