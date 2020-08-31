import math
pi = math.pi
# challenges
# 1
class Apple() :
    def __init__(self, t, c, w, a) :
        self.type = t
        self.color = c
        self.weight = w
        self.age = a
        print("Created!")

app1 = Apple("fuji", "red", 12, 6)
app2 = Apple("Golden delicious", "golden", 14, 17)
print(app2.age)
# 2
class Circle() :
    def __init__(self, r) :
        self.radius = r
        print("created!")

    def area(self) :
        return (self.radius ** 2) * pi

cir1 = Circle(2)
print(cir1.area())

# 3
class Triangle() :
    def __init__(self, l, w) :
        self.width = w
        self.len = l

    def area(self) :
        return (self.width * self.len) * 0.5
tri1 = Triangle(1,3)
print(tri1.area())
tri2 = Triangle(5,6)
print(tri2.area())

# 4
class Hexagon() :
    def __init__(self, l) :
        self.len = l

    def perimeter(self) :
        return  (self.len * 6)
hex1 = Hexagon(3)
hex2 = Hexagon(5)
print(hex1.perimeter(), hex2.perimeter())