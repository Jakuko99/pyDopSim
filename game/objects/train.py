from uuid import UUID, uuid4


class Train:
    def __init__(self, train_asset: str, train_nr: int = None):
        self.uuid: UUID = uuid4()
        self.train_asset = train_asset
        self.train_nr = train_nr
        self.carriages: list = []

    def add_carriage(self, carriage_asset: str):
        pass
