
class trackSegment:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        self.occupied = False
        self.occupiedBy = None

    @property
    def isOccupied(self):
        return self.occupied

    def occupy(self, train):
        self.occupied = True
        self.occupiedBy = train

    def changeState(self, state):
        self.occupied = state
        if self.occupied:
            # set color to red
            pass
        else:
            # set color back to gray            
            pass