class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_p(self):
        return (self.a * self.a +self.b)

    def get_s(self):
        return (1/2 * self.a * self.b)

t = Triangle(5, 6, 2)

print(t.get_p())
print(t.get_s())
