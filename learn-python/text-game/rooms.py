class Room(object):

    def __init__(self):
        pass

class Entrance(Room):

    def enter(self):
        print("Do you want to continue?")
        user_input = input(">")
        if user_input == "y":
            print("yes")

def Engine(Room):
    current_room = Room() # instantiates an instance of the current room
    current_room.enter() 

Engine(Entrance)


