from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # value
        self.company_id = "5049209"
        self.username = "qatestsalesman"
        self.password = "it.QA2025"

    # Locator
    company_id_xpath = (By.ID, "id.edot.ework:id/tv_company_id")
    username_xpath = (By.ID, "id.edot.ework:id/tv_username")
    password_xpath = (By.ID, "id.edot.ework:id/tv_password")
    signIn_button_xpath = (By.ID, "id.edot.ework:id/button_text")
    new_costumer_xpath = (By.XPATH, "(//android.widget.FrameLayout[@resource-id='id.edot.ework:id/card_icon'])[5]")

    # Action
    def enter_company_id(self):
        self.wait.until(EC.presence_of_element_located(self.company_id_xpath)).send_keys(self.company_id)

    def enter_username(self):
        self.wait.until(EC.presence_of_element_located(self.username_xpath)).send_keys(self.username)

    def enter_password(self):
        self.wait.until(EC.presence_of_element_located(self.password_xpath)).send_keys(self.password)

    def tap_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.signIn_button_xpath)).click()

    time.sleep(5)