class Cat:
    def speak(self):
        print("Meow!")


class Dog:
    def speak(self):
        print("Woof!")


pets = [Cat(), Dog(), Cat()]
for pet in pets:
    pet.speak()
