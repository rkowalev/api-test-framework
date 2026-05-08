# QA Automation Framework

[![API Tests](https://github.com/rkowalev/qa-automation-framework/actions/workflows/api-tests.yml/badge.svg)](https://github.com/rkowalev/qa-automation-framework/actions/workflows/api-tests.yml)
[![UI Tests](https://github.com/rkowalev/qa-automation-framework/actions/workflows/ui-tests.yml/badge.svg)](https://github.com/rkowalev/qa-automation-framework/actions/workflows/ui-tests.yml)
![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-8.x-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/playwright-1.58-2EAD33?logo=playwright&logoColor=white)
![Docker](https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white)
![Allure](https://img.shields.io/badge/allure-report-FE7E37?logo=qase&logoColor=white)

End-to-end test automation framework covering both API and UI layers. Built with Pytest and Playwright, packaged in Docker, integrated with GitHub Actions CI.

## Tech Stack

- **Language:** Python 3.12
- **Test framework:** Pytest, pytest-playwright, pytest-mock
- **API testing:** Requests, Pydantic (response validation), Faker (test data)
- **UI testing:** Playwright (Page Object Model pattern)
- **Reporting:** Allure
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Database:** PostgreSQL (used in compose for SQL practice)

## What's covered

- **API:** [Petstore Swagger](https://petstore.swagger.io/) — full CRUD coverage with positive, negative, and parametrized scenarios. Mocked server-error tests included.
- **UI:** [TodoMVC](https://demo.playwright.dev/todomvc) and [The Internet](https://the-internet.herokuapp.com) — login flow and todo management via Page Object Model.

## Project Structure

```
qa-automation-framework/
├── .github/workflows/         # CI configuration
│   ├── api-tests.yml
│   └── ui-tests.yml
├── models/                    # Pydantic models for API responses
│   └── pet.py
├── pages/                     # Page Object Model classes
│   ├── login_page.py
│   ├── secure_area_page.py
│   └── todo_page.py
├── tests/
│   ├── conftest.py            # Shared fixtures (HttpClient, Faker)
│   ├── api/                   # API tests (marker: api)
│   │   └── petstore/
│   └── ui/                    # UI tests (marker: ui)
│       ├── conftest.py        # Page Object fixtures
│       ├── test_login.py
│       └── test_todomvc.py
├── utils/
│   └── http_client.py         # Wrapper over requests.Session with Allure attachments
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
└── requirements.txt
```

## How to Run

### Local (Python)

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers (for UI tests)
playwright install chromium

# Run all tests
pytest

# Run only API tests
pytest -m api

# Run only UI tests
pytest -m ui

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

### Docker (API tests)

```bash
docker build -t qa-tests .
docker run --rm qa-tests pytest -m api
```

### Database (for SQL exploration)

```bash
docker compose up postgres -d
```

## CI/CD

Two GitHub Actions workflows trigger on every push and pull request to `main`:

- **API Tests** — builds Docker image from project Dockerfile and runs API tests inside the container. Verifies that the Docker setup is reproducible.
- **UI Tests** — installs Python and Playwright browsers, runs UI tests on chromium. On failure, uploads screenshots, videos, and Playwright traces as workflow artifacts for debugging.

## Reporting

UI tests are configured to capture on failure:
- Screenshots
- Video recordings
- Playwright traces (viewable in [trace.playwright.dev](https://trace.playwright.dev))

Allure reports can be generated for any test run via `--alluredir=allure-results`.

## Author

[Ruslan Kovalev](https://github.com/rkowalev)