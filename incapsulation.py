from random import randint

class Nums:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.__do_sums()
    def __do_sums(self):
        random = randint(1, 5)
        if random == 1:
            print(self.num1 + self.num2, "operation plus ")

        if random == 2:
            print(self.num1 - self.num2, "operation minus ")

        if random == 3:
            print(int(self.num1) * int(self.num2), "operation times ")

        if random == 4:
            print(self.num1 / self.num2, "operation divide ")


num = Nums(float(input("First number: ")),float(input("Second number: ")))



