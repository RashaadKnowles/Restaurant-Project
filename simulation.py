# How to create facade pattern
# Import from another class
# Call object in the initializer
# Do self. annotation to your class name and the set it equal to class and object in parenthesis
# Use dot annotation to your class and object
from franchise import Franchise
class Simulation:
    def __init__(self,) -> None:
        self.Franchise = Franchise()




    def run_simulation(self):
        self.Franchise.place_order()
        self.Franchise.place_order()
        self.Franchise.place_order()
