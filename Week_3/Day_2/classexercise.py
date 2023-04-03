class Door:
    def __init__(self,is_opened):
        self.is_opened = is_opened
    def open_door(self):
        if self.is_opened:
            print("door already opened") 
        else:
            print("Door opened")
    def close_door(self):
        if self.is_opened:
            print("Door closed") 
        else:
            print("door already closed") 
class BlockedDoor(Door):
    def __init__(self):
        pass
    def open_door(self):
        raise Exception("Blocked door can't be opened") 
    def close_door(self):
        raise Exception("Blocked door can't be closed") 
door = BlockedDoor()
door.close_door()