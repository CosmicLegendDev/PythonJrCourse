# Class and methods

class House:

    # called as init method and automatically invoked when object is created.
    def __init__(self):
        self.rooms = 5
        self.doors = 8
        self.windows = 14
        self.cieling_height = 10.5
        
        print("Object has beein initialized.")

    def print_plan(self):
        print("*" * 5 + " Your Dream Home " + "*" * 5)
        print(f"Your Home contains {self.rooms} rooms")
        print(f"Your Home height is {self.cieling_height}")

    def calculate_cost(self, wages):
        room_cost = 1 #millions
        paint_per_room = 0.5 #millions
        electrical_room = 0.2 #millions

        # total_room * room_cost + total_rooms * paint_cost + total_rooms * electrical_cost
        total_cost = (self.rooms * room_cost) + (self.rooms * paint_per_room) + (self.rooms * electrical_room)
        total_cost = total_cost + wages
        print(f"Total to build a house: {total_cost}$mil")


if __name__ == "__main__":
    my_house = House()
    my_house.print_plan()
    #print(my_house.doors)
    my_house.calculate_cost(wages=1.2)