class Animals:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

    def _catch_robber(self):
        print(f"OMG! {self.name} catch robber!")


class Cat(Animals):
    __mice = 0

    def speak(self):
        print("Meow!")

    def __catch_mouse(self):
        self.__mice += 1
        print(f"Wow! {self.name} catch mouse")


class Dog(Animals):
    def speak(self):
        print("Woof!")


class SuperCat(Cat):
    pass

murka = Cat(name="Murka", age=1)
sharik = Dog(name="Sharik", age=2)
murka.__catch_mouse()
murka._Cat__catch_mouse()
sharik._catch_robber()
murka._catch_robber()
#
# new_cat = SuperCat(name="Murka", age=1)
# pass
#
# type_ = 1
# _ = 1
#
# for _, value in {1:1, 2:2}.items():
#     print(value)
