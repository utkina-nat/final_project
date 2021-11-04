import pytest
from pages.auth_page import AuthPage

def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('q4q4test.test@yandex.ru')

    page.password.send_keys("QAqatest123")

    page.btn.click()

    assert page.get_current_url() == 'https://www.ozon.ru/'