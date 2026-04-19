import pytest
from utils.http_client import HttpClient
from faker import Faker
import random
import os

@pytest.fixture(scope="session")
def petstore_httpClient():
    return HttpClient(
        base_url = os.getenv("BASE_URL", "https://petstore.swagger.io/v2"), 
        headers={"content-type": "application/json"}
        )

@pytest.fixture
def create_pet(petstore_httpClient, fake_data):
    body = generate_random_data(fake_data)
    response = petstore_httpClient.post(endpoint="/pet", body=body)
    pet_id = response.json()["id"]
    yield response
    petstore_httpClient.delete(endpoint=f"/pet/{pet_id}")

@pytest.fixture
def fake_data():
    seed = random.randint(0, 999999)
    print(f"\nFaker seed: {seed}")
    Faker.seed(seed)
    fake_data = Faker()
    return fake_data

def generate_random_data(fake_data):
    body = {
        "id": fake_data.random_int(min=100, max=999),
        "name": fake_data.first_name(),
        "status": fake_data.random_element(["available", "pending", "sold"])
    }
    return body

