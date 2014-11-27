class Room(object):

    def __init__(self):
        pass

class Entrance(Room):


    def enter(self):

        print("""You approach the temple entrance. A large door stands before you.
        What would you like to do?""")
        action = input('> ')
        if action == "open door":
            print("You entered the temple")
            return "potato"

        
def Engine(Room):
    current_room = Room() # instantiates an instance of the current room
    current_room.enter() 


Engine(Entrance)
