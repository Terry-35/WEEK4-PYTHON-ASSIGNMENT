# Base Class: Moveable
class Moveable:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Cheetah class inherits from Moveable
class Cheetah(Moveable):
    def move(self):
        print("Running fast like a Cheetah!")

# Subaru class inherits from Moveable
class Subaru(Moveable):
    def move(self):
        print("Driving the Subaru on the road")

# Test - calling move() on each
def test_move(moveables):
    for moveable in moveables:
        moveable.move()

# Creating instances of each moveable object
cheetah = Cheetah()
subaru = Subaru()

# Testing polymorphism
test_move([cheetah, subaru])
