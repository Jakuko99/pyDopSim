class ClientSession:
    def __init__(self, client: str, client_name: str):
        self.client_ip: str = client
        self.client_name: str = client_name
