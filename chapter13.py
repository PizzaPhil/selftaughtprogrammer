#Challenges
# 1 - 3
class Shape() :
    def what_am_i(self) :
        print("I am a shape")

class Square(Shape) :
    def __init__(self, l) :
        self.length = l
    def calculate_perimeter(self) :
        return (self.length * 4)

    def change_size(self, l) :
        self.length = l

class Rectangle(Shape) :
    def __init__(self, l, w) :
        self.length = l
        self.width = w
    def calculate_perimeter(self) :
        return (self.length * 2) + (self.width * 2)

sq1 = Square(2)
rec1 = Rectangle(2,5)
print(sq1.calculate_perimeter())
print(rec1.calculate_perimeter())
sq1.change_size(4)
print(sq1.calculate_perimeter())
sq1.what_am_i()
rec1.what_am_i()


# 4
class Horse() :
    def __init__(self, r, n) :
        self.rider = r
        self.name = n


class Rider() :
    def __init__(self, n) :
        self.name = n


rider1 = Rider("Billy-Jim")
horse1 = Horse(rider1, "Hooves")
print(horse1.rider.name)








