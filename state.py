from enum import Enum

class Status(Enum):
    Main = 0
    Description = 1
    PvP = 2
    Ai = 3

class State:
    def __init__(self, initial_status=Status.Main):
        self.status = initial_status