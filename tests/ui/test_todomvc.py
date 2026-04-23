from playwright.sync_api import Page, expect


def test_add_single_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")

    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Buy milk")
    todo_input.press("Enter")

    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(page.get_by_test_id("todo-item")).to_have_text("Buy milk")

def test_delete_item(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")

    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Buy milk")
    todo_input.press("Enter")
    
    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(page.get_by_test_id("todo-item")).to_have_text("Buy milk")
    expect(page.get_by_test_id("todo-item")).to_be_visible()

    page.get_by_test_id("todo-item").hover()
    page.get_by_role("button", name="Delete").click()

    expect(page.get_by_test_id("todo-item")).not_to_be_visible()
    expect(page.get_by_test_id("todo-item")).to_have_count(0)

def test_correct_text_of_list_numbers(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")
    todo_input = page.get_by_placeholder("What needs to be done?")

    todo_input.fill("test1")
    todo_input.press("Enter")

    expect(page.get_by_test_id("todo-count")).to_have_text("1 item left")

    todo_input.fill("test2")
    todo_input.press("Enter")
    todo_input.fill("test3")
    todo_input.press("Enter")

    expect(page.get_by_test_id("todo-count")).to_have_text("3 items left")

    task1 = page.get_by_test_id("todo-item").filter(has_text="test1")
    task1.get_by_role("checkbox").check()

    expect(page.get_by_test_id("todo-count")).to_have_text("2 items left")
