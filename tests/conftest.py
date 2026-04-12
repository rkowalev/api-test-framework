import pytest
from utils.http_client import HttpClient

@pytest.fixture(scope="session")
def petstore_httpClient():
    return HttpClient(
        base_url = "https://petstore.swagger.io/v2", 
        headers={"content-type": "application/json"}
        )

@pytest.fixture
def create_pet(petstore_httpClient):
    response = petstore_httpClient.post(endpoint="/pet", body={"id": 228, "name": "Flash", "photoUrls": ["string"]})
    pet_id = response.json()["id"]
    yield response
    petstore_httpClient.delete(endpoint=f"/pet/{pet_id}")
