class Solve():
    def __init__(self):
        self.all = []
        self.price = 0
        self.total = 0

        with open("Langdat/prog213b.txt", "r") as f:
            for line in f:
                self.all.append(int(line))

    def calc(self):
        for x in self.all:
            if x in range(0, 101):
                self.price = 5.95
            elif x in range(101,200):
                self.price = 5.75
            elif x in range(200,300):
                self.price = 5.40
            elif x in range(300, 100000000):
                self.price = 5.15
            self.total = x * self.price

            print(f"Quantiy    :  {x}")
            print(f"Your price :  ${self.price}")
            print(f"Your total :  ${self.total:.2f}\n")
