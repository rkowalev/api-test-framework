from playwright.sync_api import Page, expect
import pytest
import re

pytestmark = pytest.mark.ui

def test_login_with_valid_credentials(login_page, secure_area_page):
    login_page.open()
    login_page.login(username="tomsmith", password="SuperSecretPassword!")
    
    expect(secure_area_page.flash_message).to_contain_text("You logged into a secure area!")
    expect(secure_area_page.page).to_have_url(re.compile(secure_area_page.URL_PART))

def test_login_with_invalid_password(login_page):
    login_page.open()
    login_page.login(username="tomsmith", password="dfsdfsdf")

    expect(login_page.page).to_have_url(login_page.URL)
    expect(login_page.flash_message).to_contain_text("Your password is invalid!")


