import requests


class PetStoreClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.setdefault("Content-Type", "application/json")
        self.session.headers.setdefault("Accept", "application/json")

    def request(self, method: str, path: str, **kwargs):
        path = path if path.startswith("/") else f"/{path}"
        url = f"{self.base_url}{path}"
        return self.session.request(method, url, **kwargs)
