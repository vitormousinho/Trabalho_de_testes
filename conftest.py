import pytest

from utils.api_client import PetStoreClient

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def api_client(base_url: str) -> PetStoreClient:
    return PetStoreClient(base_url)
