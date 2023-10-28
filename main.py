#1

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")


if __name__ == "__main__":
    elevator = Elevator(1, 10)
    target_floor = 5
    elevator.go_to_floor(target_floor)
    elevator.go_to_floor(1)

#2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        elevator = self.elevators[elevator_num - 1]
        elevator.go_to_floor(destination_floor)


if __name__ == "__main__":
    building = Building(1, 10, 2)
    building.run_elevator(1, 5)
    building.run_elevator(2, 7)


#3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        elevator = self.elevators[elevator_num - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


if __name__ == "__main__":
    building = Building(1, 10, 2)
    building.run_elevator(1, 5)
    building.run_elevator(2, 7)
    print("\nFire alarm triggered!")
    building.fire_alarm()

#4

import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"| {self.registration_number:12} | {self.maximum_speed:13} | {self.current_speed:12} | {self.travelled_distance:17} |"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print("| Registration | Maximum Speed | Current Speed | Travelled Distance |")
        print("-" * 60)
        for car in self.cars:
            print(car)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = random.randint(100, 200)
        cars.append(Car(registration_number, maximum_speed))

    grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)

    hour = 1
    while not grand_demolition_derby.race_finished():
        grand_demolition_derby.hour_passes()
        if hour % 10 == 0:
            print(f"\nStatus after {hour} hours:")
            grand_demolition_derby.print_status()
        hour += 1

    print("\nFinal Race Status:")
    grand_demolition_derby.print_status()
