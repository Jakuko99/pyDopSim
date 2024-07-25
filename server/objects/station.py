from uuid import UUID, uuid4

from server.data_types.api_package import StationStatus


class Station:
    uid: UUID = uuid4()
    station_name: str
    left_station: str
    right_station: str
    turn_station: str
    station_type: str
    status: StationStatus = StationStatus.OFFLINE
    player_name: str = None
    route_uid: UUID = None
    station_inflections: str = None

    def __dict__(self) -> dict:
        return {
            "uid": str(self.uid),
            "station_name": self.station_name,
            "left_station": self.left_station,
            "right_station": self.right_station,
            "turn_station": self.turn_station,
            "status": self.status.value,
            "station_type": self.station_type,
            "player_name": self.player_name,
            "route_uid": str(self.route_uid),
            "station_inflections": self.station_inflections,
        }

    def __list__(self) -> list:
        return [
            str(self.uid),
            self.station_name,
            self.left_station,
            self.right_station,
            self.turn_station,
            self.status.value,
            self.station_type,
            self.player_name,
            str(self.route_uid),
            self.station_inflections,
        ]
