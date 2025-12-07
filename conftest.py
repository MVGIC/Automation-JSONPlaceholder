import pytest
from utils.api_helper import APIClient

API_URL = "https://jsonplaceholder.typicode.com/"

@pytest.fixture()
def api_client():
    """
    Создать API для теста

    """
    client = APIClient()
    yield client