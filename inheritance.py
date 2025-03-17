class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("HI")

    def __str__(self):
        return "Animal"


class Cat(Animal):
    # Cat inherits name, age, and say_hi from Animal
    def __init__(self, name, age, sound):
        # Animal.__init__(name, age)
        super().__init__(name, age)
        self.sound = sound

    def say_sound(self):
        print(self.sound)

    def __str__(self):
        return "Cat: " + self.name


cat = Cat("Fish", 5, "MEOW")
cat.say_hi()
cat.say_sound()
print(cat)

