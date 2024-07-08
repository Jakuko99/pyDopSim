from uuid import UUID, uuid4

from server.data_types.api_package import StationStatus


class Station:
    def __init__(
        self,
        station_name: str,
        left_station: str,
        right_station: str,
        turn_station: str = None,
        station_type: str = None,
    ):
        self.uuid: UUID = uuid4()
        self.station_name: str = station_name
        self.left_station: str = left_station
        self.right_station: str = right_station
        self.turn_station: str = turn_station
        self.status: StationStatus = StationStatus.OFFLINE
        self.station_type: str = station_type

        self.station_name_N: str = self.station_name
        self.station_name_G: str = None
        self.station_name_L: str = None

        self.player_name: str = None

    def add_inflections(self, station_name_G: str, station_name_L: str):
        self.station_name_G = station_name_G
        self.station_name_L = station_name_L

    def set_player_name(self, name: str):
        self.player_name = name

    def __dict__(self):
        return {
            "uuid": str(self.uuid),
            "station_name": self.station_name,
            "left_station": self.left_station,
            "right_station": self.right_station,
            "turn_station": self.turn_station,
            "status": self.status.value,
            "station_type": self.station_type,
            "station_name_N": self.station_name_N,
            "station_name_G": self.station_name_G,
            "station_name_L": self.station_name_L,
            "player_name": self.player_name,
        }
