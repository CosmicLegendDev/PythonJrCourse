# Define a class

class House:

    # called as init method and automatically invoked when object is created.
    def __init__(self):
        self.rooms = 5
        self.doors = 8
        self.windows = 14
        self.room_height = 10.5
        self.room_width = {
            "room1width": 13.5,
            "room3width": 14.5
        }
        print("Object has beein initialized.")

if __name__ == "__main__":
    # How to create an object from House class.
    my_house = House()
    print(type(my_house))