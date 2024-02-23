import time


class Pet:
    def __init__(self,age,weight,energy):
        self.age = age
        self.weight = weight
        self.energy = energy
    def play(self, hours):
        print("Playing...")
        self.energy -= hours * 0.5
        self.weight -= hours * 0.5
        time.sleep(2)

    def eat(self, hours):
        print("Eating...")
        self.weight += hours * 0.5
        self.energy += hours * 0.5
        time.sleep(2)

    def sleep(self, hours):
        print("Sleeping...")
        self.age += hours * 0.2
        self.energy += hours * 0.5
        time.sleep(2)




cat = Pet(1,5,0.2)
dog = Pet(4,7,10)

q = input("What animal do you want to play for cat/dog?")

if q == "cat":
    game = float(input("How many hours will cat play: "))
    cat.play(game)

    lunch = float(input("How many hours will cat eat: "))
    cat.eat(lunch)

    sleeping = float(input("How many hours will cat sleep: "))
    cat.sleep(sleeping)

    print(f"Weight:{cat.weight}, Age:{cat.age}, Energy:{cat.energy}")

elif q == "dog":
    game = float(input("How many hours will dog play: "))
    dog.play(game)

    lunch = float(input("How many hours will dog eat: "))
    dog.eat(lunch)

    sleeping = float(input("How many hours will dog sleep: "))
    dog.sleep(sleeping)

    print(f"Weight:{dog.weight}, Age:{dog.age}, Energy:{dog.energy}")