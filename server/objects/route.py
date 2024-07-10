from uuid import uuid4, UUID


class Route:
    uid: UUID = uuid4()
    route_name: str

    def __dict__(self) -> dict:
        return {
            "uuid": str(self.uuid),
            "route_name": self.route_name,
        }
