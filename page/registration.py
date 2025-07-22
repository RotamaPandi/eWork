from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # value input
        self.outline_name = "QA Costumer"
        self.outline_phone = "8348889777"
        self.outline_email = "qacostumer@gmail.com"
        self.contact_person = "qa"

    # locator
    new_costumer_menu_xpath = (By.XPATH, "(//android.widget.FrameLayout[@resource-id='id.edot.ework:id/card_icon'])[5]")
    new_costumer_registration_id = (By.ID, "id.edot.ework:id/tvRegister")

    outline_name_id = (By.ID, "id.edot.ework:id/et_outlet_name")
    outline_phone_id = (By.ID, "id.edot.ework:id/et_outlet_phone")
    outline_email_id = (By.ID, "id.edot.ework:id/et_outlet_email")
    contact_person_id = (By.ID, "id.edot.ework:id/et_contact_person")

    channel_id = (By.ID, "id.edot.ework:id/et_channel")
    choose_channel_xpath = (By.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Modern Trade (MT)']")

    costumer_type_id = (By.ID, "id.edot.ework:id/et_outlet_type")
    choose_costumer_xpath = (By.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Grosir']")

    continue_btn_id = (By.ID, "id.edot.ework:id/button_text")

    # method scroll
    def scroll_to_text(self, text):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )

    # actions
    def new_costumer_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.new_costumer_menu_xpath)).click()

    def new_costumer_registration(self):
        self.wait.until(EC.element_to_be_clickable(self.new_costumer_registration_id)).click()

    def fill_form(self):
        self.wait.until(EC.presence_of_element_located(self.outline_name_id)).send_keys(self.outline_name)
        self.wait.until(EC.presence_of_element_located(self.outline_phone_id)).send_keys(self.outline_phone)
        self.wait.until(EC.presence_of_element_located(self.outline_email_id)).send_keys(self.outline_email)
        self.wait.until(EC.presence_of_element_located(self.contact_person_id)).send_keys(self.contact_person)

        # channel dropdown
        self.wait.until(EC.element_to_be_clickable(self.channel_id)).click()
        self.scroll_to_text("Modern Trade (MT)")
        self.wait.until(EC.element_to_be_clickable(self.choose_channel_xpath)).click()

        # costumer type dropdown
        self.wait.until(EC.element_to_be_clickable(self.costumer_type_id)).click()
        self.scroll_to_text("Grosir")
        self.wait.until(EC.element_to_be_clickable(self.choose_costumer_xpath)).click()

        # scroll to continue button
        self.scroll_to_text("Lanjutkan")
        self.wait.until(EC.element_to_be_clickable(self.continue_btn_id)).click()
