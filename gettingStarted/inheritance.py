class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def eat(self):
        print("animal eating")

    def speak(self):
        print("animal speaking")


class Bird(Animal):
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def eat(self):
        print("animal eating")

    def speak(self):
        print("animal speaking")


class Fish(Animal):



class Eagle(Bird):