from playwright.sync_api import Page, expect

def test_add_single_todo(todo_page):
    todo_page.open()
    todo_page.add_todo_item("bye milk")

    expect(todo_page.item).to_have_count(1)
    expect(todo_page.item).to_have_text("bye milk")

def test_delete_item(todo_page):
    todo_page.open()
    todo_page.add_todo_item("bye milk")

    expect(todo_page.item).to_have_count(1)
    expect(todo_page.item).to_be_visible()

    todo_page.delete_todo_item("bye milk")

    expect(todo_page.item).to_have_count(0)

def test_correct_text_of_list_numbers(todo_page):
    todo_page.open()
    todo_page.add_todo_item("test 1")

    expect(todo_page.counter).to_have_text("1 item left")

    todo_page.add_todo_item("test 2")
    todo_page.add_todo_item("test 3")

    expect(todo_page.counter).to_have_text("3 items left")

    todo_page.delete_todo_item("test 2")

    expect(todo_page.counter).to_have_text("2 items left")