from uuid import UUID, uuid4

from game.data_types.api_package import TrainType


class Train:
    uid: UUID = uuid4()
    train_number: int
    train_type: TrainType
    station_uid: UUID

    def __dict__(self) -> dict:
        return {
            "uuid": str(self.uid),
            "train_number": self.train_number,
            "train_type": self.train_type,
            "station_uid": str(self.station_uid),
        }
