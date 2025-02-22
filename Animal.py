class Animal:
    def __init__(self, name, species="Unknown", age=0, sound="Silent"):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def talk(self):
        print(f"{self.name} says: {self.sound}")

    def eat(self, food="food"):
        print(f"{self.name} is eating {food}.")

    def sleep(self, hours=8):
        print(f"{self.name} is sleeping for {hours} hours.")

    # Fixed functions with optional parameters
    def play(self, activity="playing"):
        print(f"{self.name} is {activity} happily!")

    def run(self, speed="fast"):
        print(f"{self.name} is running {speed}!")

    def grow_older(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

    def change_sound(self, new_sound):
        self.sound = new_sound
        print(f"{self.name} now makes this sound: {self.sound}")

    def describe(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Sound: {self.sound}")
