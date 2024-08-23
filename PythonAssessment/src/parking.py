import re

FREE_SLOT = "_"
BUSSY_SLOT = "x"

class Parking:

    def __init__(self, size: int):
        self.parking_grid = []
        self.free_slot = FREE_SLOT
        self.bussy_slot = BUSSY_SLOT
        self.fill_parking(size)
        self.size = size

    def fill_parking(self, size):
        self.parking_grid = [[FREE_SLOT for _ in range(size)] for _ in range(size)]

    def print_parking(self):
        for parking_row in self.parking_grid:
            print(re.sub(r'\[|\]|,', '|', str(parking_row)))
        print("\n")
