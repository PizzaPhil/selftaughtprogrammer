# challenges
# 1
class Square() :
    square_list = []
    def __init__(self, len) :
        self.length = len
        self.square_list.append((self.length, self.length))
# 2
    def __repr__(self) :
        return ("this square is " + str(self.length) + " by " + str(self.length) + " by " + str(self.length) + " by " + str(self.length))

sq1 = Square(2)
sq2 = Square(4)

print(Square.square_list)
print(sq1)

# 3
def is_same(one, two) :
    if one is two :
        print("They're the same!")

    if one is not two :
        print("they ain't same")



is_same(sq1,sq2)