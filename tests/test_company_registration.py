import pytest
import time

from utils.driver_setup import init_driver
from page.login import LoginPage
from page.registration import RegistrationPage


@pytest.fixture(scope="session")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)

    login_page.enter_company_id()
    login_page.enter_username()
    login_page.enter_password()
    login_page.tap_sign_in()

    time.sleep(3)

def test_company_registration(driver):
    reg = RegistrationPage(driver)

    reg.new_costumer_menu()
    reg.new_costumer_registration()
    reg.fill_form()

    time.sleep(5)
