
class VisualButton():
    def __init__(self, x : int, y : int, routine : function, **kwargs) -> None:
        self.x = x
        self.y = y
        self.routine = routine