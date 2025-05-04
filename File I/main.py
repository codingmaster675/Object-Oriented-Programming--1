class parrot:
    species="bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age
blue=parrot("blue", 5)
green=parrot("green", 6)
print("Blue is a {}".format(blue.species))
print("Green is a {}".format(green.species))
print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(green.name, green.age))