from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     page = context.new_page()

#     page.goto("https://demo.playwright.dev/todomvc")

#     # Пробуем четыре способа найти одно и то же поле ввода
#     by_role        = page.get_by_role("textbox", name="What needs to be done?")
#     by_placeholder = page.get_by_placeholder("What needs to be done?")
#     by_text        = page.get_by_text("What needs to be done?")
#     by_css         = page.locator(".new-todo")

#     # .count() — сколько элементов нашлось по каждому локатору
#     print(f"by_role:        {by_role.count()}")
#     print(f"by_placeholder: {by_placeholder.count()}")
#     print(f"by_text:        {by_text.count()}")
#     print(f"by_css:         {by_css.count()}")

#     input("Нажми Enter чтобы закрыть браузер...")
#     browser.close()

#     from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=500)

#     # Контекст #1: десктоп, русский язык
#     desktop_context = browser.new_context(
#         viewport={"width": 1920, "height": 1080},
#         locale="ru-RU"
#     )
#     desktop_page = desktop_context.new_page()
#     desktop_page.goto("https://www.google.com")

#     # Контекст #2: мобилка, английский
#     mobile_context = browser.new_context(
#         viewport={"width": 375, "height": 667},
#         locale="en-US",
#         user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15"
#     )
#     mobile_page = mobile_context.new_page()
#     mobile_page.goto("https://www.google.com")

#     input("Сравни две вкладки и нажми Enter...")

#     browser.close()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demo.playwright.dev/todomvc")

    # Добавить задачу
    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Learn Playwright")
    todo_input.press("Enter")

    # Добавить ещё две
    todo_input.fill("Buy groceries")
    todo_input.press("Enter")

    todo_input.fill("Call mom")
    todo_input.press("Enter")

    input("Посмотри на браузер и нажми Enter для закрытия...")
    browser.close()