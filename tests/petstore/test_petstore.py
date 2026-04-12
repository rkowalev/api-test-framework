import pytest
import allure
from models.pet import Pet
import json

@allure.feature("Pet tests CRUD")
class TestPetCrud():
    @allure.story("Pet Post test")
    def test_post(self, petstore_httpClient):
        body = {"id": 228, "name": "Flash", "photoUrls": ["string"]}
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
            assert response.status_code == 200
