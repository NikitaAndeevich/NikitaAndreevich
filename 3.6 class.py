class Animals:
    horns = 0
    paws = 0
    food = ""
    produce = ""
    weight = 0
    sound = "Mooo!"

    def say(self):
        print(self.sound)

    def __init__(self, horns, paws, food, produce, weight):
        self.horns = horns
        self.paws = paws
        self.food = food
        self.produce = produce
        self.weight = weight


class Cows(Animals):
    sound = "Mooo!"


class Goats(Animals):
    sound = "Meee!"


class Sheeps(Animals):
    sound = "Beee!"


class Pigs(Animals):
    sound = "oink oink!"


class Ducks(Animals):
    sound = "quack quack!"


class Chickens(Animals):
    sound = "peep peep!"


class Geeses(Animals):
    sound = "honk honk!"


cow = Cows(2, 4, "hay", "meat, milk", 1500)
print(cow.__dict__)
print(cow.sound)

goat = Goats(2, 4, "hay", "meat, milk", 300)
print(goat.__dict__)
print(goat.sound)

sheep = Sheeps(2, 4, "hay", "meat, wool", 250)
print(sheep.__dict__)
print(sheep.sound)

pig = Pigs(0, 4, "hay", "meat", 500)
print(pig.__dict__)
print(pig.sound)

duck = Ducks(0, 2, "insects", "meat", 30)
print(duck.__dict__)
print(duck.sound)

chicken = Chickens(0, 2, "corn", "meat, eggs", 15)
print(chicken.__dict__)
print(chicken.sound)

geese = Geeses(0, 2, "insects", "meat", 40)
print(geese.__dict__)
print(geese.sound)