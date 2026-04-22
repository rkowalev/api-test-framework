from playwright.sync_api import Page, expect


def test_add_single_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")

    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Buy milk")
    todo_input.press("Enter")

    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(page.get_by_test_id("todo-item")).to_have_text("Buy milk")