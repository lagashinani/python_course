class Animal():
    def __init__(self, name, weight=None):
        self.name = name
        self.weight = weight

    def feed(self):
        print(self.name + " feeded")

    def getWeight(self):
        return self.weight

class Bird(Animal):
    def collect(self):
        print("Eggs collected")


class Goose(Bird):
    def say(self):
        print("GaGaGa")

class Cow(Animal):
    def say(self):
        print("Muuuuuuuuuuuuuuuu")

    def collect(self):
        print("Milk collected")

class Sheep(Animal):
    def say(self):
        print("Beeeeee")

    def collect(self):
        print("Wool trimmed")

class Chicken(Bird):
    def say(self):
        print("KoKoKoKoKo")

class Goat(Animal):
    def say(self):
        print("Meeeeee")

    def collect(self):
        print("Milk collected")

class Duck(Bird):
    def say(self):
        print("KryaKrya")


Animals = {"Seriy": Goose("Серый", 7),
           "Beliy": Goose("Белый", 6),
           "Manka": Cow("Манька", 670),
           "Barashek": Sheep("Барашек", 100),
           "Kydryaviy": Sheep("Кудрявый", 101),
           "KoKo": Chicken("Ко-Ко", 1.1),
           "Kukareku": Chicken("Кукареку", 0.8),
           "Roga": Goat("Рога", 80),
           "Kopita": Goat("Копыта", 70),
           "Kryakva": Duck("Кряква", 1.2),
           }

for name, animal in Animals.items():
    animal.feed()
    animal.collect()
    animal.say()



summ = sum(map(lambda x: x.getWeight(), Animals.values()))
print("Total weight: " + str(summ))
print("The heaviest: " + max(Animals.values(), key=lambda x: x.getWeight()).name)