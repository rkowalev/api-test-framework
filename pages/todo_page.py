from playwright.sync_api import Page, Locator

class TodoPage:
    URL = "https://demo.playwright.dev/todomvc"

    def __init__(self, page: Page):
        self.page = page

        self.todo_input: Locator = page.get_by_placeholder("What needs to be done?")
        self.item: Locator = page.get_by_test_id("todo-item")
        self.counter: Locator = page.get_by_test_id("todo-count")

    def open(self):
        self.page.goto(self.URL)

    def add_todo_item(self, text):
        self.todo_input.fill(text)
        self.todo_input.press("Enter")

    def delete_todo_item(self, text):
        task = self.item.filter(has_text=text)
        task.hover()
        task.get_by_role("button", name="Delete").click()

    def check_todo_item(self, text):
        task = self.item.filter(has_text=text)
        task.get_by_role("checkbox", name="Toggle Todo").check()