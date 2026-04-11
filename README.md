# API Test Framework

Automated API testing framework using Python, Pytest, Pydantic, and Allure.

## Stack
- Python 3.14
- Pytest
- Requests
- Pydantic
- Allure
- pytest-mock

## APIs under test
- [Petstore Swagger](https://petstore.swagger.io/)
- [Reqres.in](https://reqres.in/)

## Run tests
```bash
pytest --alluredir=allure-results
allure serve allure-results
```