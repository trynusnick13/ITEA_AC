class Car:
    _car_hood_opening = 0
    __software_version = 1

    def __init__(self):
        self.__tires_diameter = 15
        self.__update_software()

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

    def _set_tires_diameter(self, diameter):
        self.__tires_diameter = diameter
        print(
            f"Successfully install custom tires diameter "
            f"{self.__tires_diameter}"
        )

    def _set_default_tires(self):
        self.__tires_diameter = 15

    def __update_software(self):
        self.__software_version += 0.5
        print(f"updating software version to {self.__software_version}")


tesla_car = Car()
tesla_car.drive()
tesla_car._open_car_hood()
tesla_car.drive()
tesla_car._open_car_hood()
tesla_car._Car__update_software()


tesla_car.get_tires_diameter()
tesla_car._set_tires_diameter(diameter=21)
tesla_car._set_default_tires()

type_ = 1

name, *_ = ("Sergey", "Surname", "asdf")

