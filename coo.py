class Cat:

    def calc(self):
        add = self.snacks + self.feet

        return add

    def __init__(self, snacks, feet):
        self.snacks = snacks
        self.feet = feet



nip = Cat(20, 4)

go = nip.calc()

print(go)
print(nip)