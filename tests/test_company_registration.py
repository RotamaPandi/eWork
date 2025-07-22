import pytest
import time
import allure

from utils.driver_setup import init_driver
from page.login import LoginPage
from page.registration import RegistrationPage


@pytest.fixture(scope="session")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()

@allure.feature("Login")
@allure.story("User can login successfully")
def test_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Fill login form"):
        login_page.enter_company_id()
        login_page.enter_username()
        login_page.enter_password()

    with allure.step("Tap Sign In"):
        login_page.tap_sign_in()

    time.sleep(3)

@allure.feature("Registration")
@allure.story("User can register new customer")
def test_company_registration(driver):
    reg = RegistrationPage(driver)

    with allure.step("Open new customer menu"):
        reg.new_costumer_menu()
    with allure.step("Open registration form"):
        reg.new_costumer_registration()
    with allure.step("Fill registration form"):
        reg.fill_form()

    time.sleep(5)
