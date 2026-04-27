import pytest
from playwright.sync_api import Page
from pages.todo_page import TodoPage

@pytest.fixture
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)