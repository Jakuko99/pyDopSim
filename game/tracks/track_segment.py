class TrackSegment:
    occupied = False
    occupied_by = "free"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y        
    
    @property
    def isOccupied(self):
        return self.occupied

    def occupiedBy(self):
        return self.occupied_by

    def occupy(self, train : str):
        self.occupied = True
        self.occupied_by = train
        self._changeState(self.occupied)

    def free(self):
        self.occupied = False
        self.occupied_by = "free"
        self._changeState(self.occupied)

    def _changeState(self, state : bool):
        self.occupied = state