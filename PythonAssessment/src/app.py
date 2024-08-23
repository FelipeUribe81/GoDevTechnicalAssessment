from parking import Parking
from car import CarInParking

if __name__ == "__main__":
    
    # Initial values
    car_initial_position = {"row": 3, "column": 2}
    car_initial_direcction = 0
    parking_size = 4

    # Initialize parking
    four_size_parking = Parking(parking_size)

    # Initialize car in parking
    car_in_parking = CarInParking(four_size_parking)
    car_in_parking.locate_car_in_parking(car_initial_position, car_initial_direcction)

    # Car in parking initial state
    print("Initial State")
    four_size_parking.print_parking()
    
    # Run movements
    car_movements = 5

    print("Car Movements")
    for i in range(car_movements):
        car_in_parking.turn_car()
        four_size_parking.print_parking()
        car_in_parking.move_forward()
        four_size_parking.print_parking()
    
    print("Final Result")
    four_size_parking.print_parking()
