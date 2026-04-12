import requests
import allure
import json 

class HttpClient():
    def __init__(self, base_url, headers=None, timeout=3):
        self.timeout = timeout
        self.session = requests.Session()

        if headers:
            self.session.headers.update(headers)
        if not base_url:
            raise ValueError("URL не может быть пустой")
        self.base_url = base_url

                
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, timeout=self.timeout)

        allure.attach(url, name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Status code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )
        return response

    def post(self, endpoint, body):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, timeout=self.timeout, json=body)

        allure.attach(url, name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Status code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )
        return response
    
    def put(self, endpoint, body):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, timeout=self.timeout, json=body)

        allure.attach(url, name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Status code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )
        return response
    
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=self.timeout)

        allure.attach(url, name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Status code", attachment_type=allure.attachment_type.TEXT)
        try:
            allure.attach(
                json.dumps(response.json(), indent=2),
                name="Response body",
                attachment_type=allure.attachment_type.JSON
                )
        except (TypeError, ValueError):
            pass
        return response