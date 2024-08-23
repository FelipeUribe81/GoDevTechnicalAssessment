from parking import Parking

# CAR_DIRECCTIONS = {0: ">", 90: "^", 180: "<", 270: "v"}
CAR_DIRECCTIONS = {
    0: {"label": ">", "forward": {"row_val": 0, "column_val": 1}, "backward": {"row_val": 0, "column_val": -1}}, 
    90: {"label": "^", "forward": {"row_val": -1, "column_val": 0}, "backward": {"row_val": 1, "column_val": 0}}, 
    180: {"label": "<", "forward": {"row_val": 0, "column_val": -1}, "backward": {"row_val": 0, "column_val": 1}},
    270: {"label": "v", "forward": {"row_val": 1, "column_val": 0}, "backward": {"row_val": -1, "column_val": 0}}
}

class CarInParking:
    
    def __init__(self, parking: Parking):
        self.car_position = {"row": 0, "column": 0}
        self.car_direcction = 0
        self.spaces_visited = 0
        self.parking = parking

    def locate_car_in_parking(self, car_position: dict, car_direcction: int):
        if self.validate_car_in_parking_limits(car_position):
            self.parking.parking_grid[car_position["row"]][car_position["column"]] = CAR_DIRECCTIONS[car_direcction]["label"]
            self.car_position = car_position
            self.car_direcction = car_direcction

    def validate_car_in_parking_limits(self, car_position: dict):
        if 0 <= car_position["row"] < self.parking.size and 0 <= car_position["column"] < self.parking.size:
            return True
        return False
    
    def move_forward(self):
        car_step_forward = CAR_DIRECCTIONS[self.car_direcction]["forward"]
        target_position = {"row": self.car_position["row"] + car_step_forward["row_val"], 
                           "column": self.car_position["column"] + car_step_forward["column_val"]}
        
        if not self.validate_car_in_parking_limits(target_position):
            return
        
        self.parking.parking_grid[target_position["row"]][target_position["column"]] = CAR_DIRECCTIONS[self.car_direcction]["label"]
        self.spaces_visited += 1
        if self.spaces_visited % 2 == 0:
            self.parking.parking_grid[self.car_position["row"]][self.car_position["column"]] = self.parking.bussy_slot
        else:
            self.parking.parking_grid[self.car_position["row"]][self.car_position["column"]] = self.parking.free_slot
            
        self.car_position = target_position
    
    def turn_car(self):
        car_look_backward = CAR_DIRECCTIONS[self.car_direcction]["backward"]
        target_position = {"row": self.car_position["row"] + car_look_backward["row_val"], 
                           "column": self.car_position["column"] + car_look_backward["column_val"]}
        
        if not self.validate_car_in_parking_limits(target_position):
            return
        
        space_behind = self.parking.parking_grid[target_position["row"]][target_position["column"]]

        if space_behind == self.parking.free_slot:
            self.car_direcction = (self.car_direcction + 90) % 360
        elif space_behind == self.parking.bussy_slot:
            self.car_direcction = (self.car_direcction - 90) % 360
        self.parking.parking_grid[self.car_position["row"]][self.car_position["column"]] = CAR_DIRECCTIONS[self.car_direcction]["label"]
