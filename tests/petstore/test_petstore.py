import pytest
import allure
from models.pet import Pet
import json
from tests.conftest import generate_random_data

@allure.feature("Pet tests CRUD")
class TestPetCrud():
    @allure.story("Pet Post test")
    def test_post(self, petstore_httpClient, fake_data):
        body = generate_random_data(fake_data)
        allure.attach(
            json.dumps(body, indent=2),
            name="Тело запроса",
            attachment_type=allure.attachment_type.JSON
        )
        with allure.step("Получение ответа на пост запрос"):
            response = petstore_httpClient.post(endpoint="/pet", body=body)
        pet = Pet.model_validate(response.json())
        
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200
        with allure.step("Поле id не пустое"):
            assert pet.id is not None


    @allure.story("Pet get test")
    def test_get(self, petstore_httpClient, create_pet):
        pet_id = create_pet.json()["id"]
        with allure.step("Получение ответа на гет запрос"):
            response = petstore_httpClient.get(f"/pet/{pet_id}")
        assert response.status_code == 200
        pet = Pet.model_validate(response.json())

        with allure.step("Проверка статус кода"):
            assert response.status_code == 200
        with allure.step("Проверка поля айди"):
            assert pet.id == pet_id

    @allure.story("Pet put test")
    def test_put(self, petstore_httpClient, create_pet):
        pet_id = create_pet.json()["id"]
        body = {"id": pet_id, "name": "Tuzik", "photoUrls": ["string"]}
        allure.attach(
            json.dumps(body, indent=2),
            name="Тело запроса",
            attachment_type=allure.attachment_type.JSON
        )
        with allure.step("Получение ответа на пут запрос"):
            response = petstore_httpClient.put(endpoint=f"/pet", body=body)
        pet = Pet.model_validate(response.json())

        with allure.step("Проверка статус кода"):
            assert response.status_code == 200
        with allure.step("Проверка апдейта поля name"):
            assert pet.name == "Tuzik"

    @allure.story("Pet delete test")
    def test_delete(self, petstore_httpClient):
        body = {"id": 999, "name": "ToDelete", "photoUrls": ["string"]}
        post_response = petstore_httpClient.post("/pet", body)
        assert post_response.status_code == 200
        with allure.step("Получение ответа на делит запрос"):
            response = petstore_httpClient.delete("/pet/999")
        with allure.step("Проверка статус кода"):
            assert response.status_code in (200, 404)

@allure.feature("Negative tests")
class TestNegativeTests():
    @allure.story("Check error status code get")
    def test_get_error(self, petstore_httpClient):
        with allure.step("Get response with wrong endpoint"):
            response = petstore_httpClient.get("/pet/9999")
        with allure.step("check status code"):
            assert response.status_code in (200, 404)

    @allure.story("check error status code delete")    
    def test_delete_error(self, petstore_httpClient):
        with allure.step("Get response with wrong endpoint"):
            response = petstore_httpClient.delete("/pet/865823685628126")
        with allure.step("check status code"):
            assert response.status_code == 404

@allure.feature("Parametrize tests")
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status(petstore_httpClient, status):
    with allure.step(f"Get pets by status {status}"):
        response = petstore_httpClient.get(f"/pet/findByStatus?status={status}")
    with allure.step("Check status code"):
        assert response.status_code == 200
