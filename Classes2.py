class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, number):
        real = self.real + number.real
        img = self.img + number.img
        result = Complex(real, img)
        return result
n1 = Complex(5, 6)
n2 = Complex(-4, 2)
result = n1.add(n2)
print("real =", result.real)
print("img =", result.img)