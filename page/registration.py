from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # value input
        self.outline_name = "QA Costumer"
        self.outline_phone = "8348889777"
        self.outline_email = "qacostumer@gmail.com"
        self.contact_person = "qa"
        self.address_fill = "Jl. Laguna Street Address"
        self.enter_ktp = "1122334455667788"

    # locator for basic form
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

    #locator for location form
    address_type_id = (By.ID, "id.edot.ework:id/et_address_type")
    choose_address_xpath = (By. XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Delivery Address']")

    address_fill_id = (By.ID, "id.edot.ework:id/etAddress")

    province_xpath = (By. XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Province']")
    choose_province_xpath = (By. XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='SULAWESI UTARA']")

    city_xpath = (By.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose City']")
    choose_city_xpath = (By. XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='KOTA MANADO']")

    district_xpath = (By.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose District']")
    choose_district_xpath = (By.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='WENANG']")

    subdistrict_xpath = (By. XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Sub district']")
    choose_subdistrict_xpath = (By.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='WENANG UTARA']")

    postal_code_xpath = (By. XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Postal code']")
    choose_postal_code_xpath = (By. XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name']")

    continue_btn_xpath = (By.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Continue']")

    #for document form
    ktp_id = (By.ID, "id.edot.ework:id/etInput")
    upload_file_btn = (By.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Upload File']")
    allow_to_access_camera = (By.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/btn_positive']")
    btn_capture_id = (By.ID, "id.edot.ework:id/btn_capture")
    submit_btn_xpath = (By.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Submit']")

    #for approval signature
    sign_here_id = (By.ID, "id.edot.ework:id/signature_view")
    register_btn_xpath = (By.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Register']")
    dc_yes_xpath = (By.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Yes']")





    # method scroll
    def scroll_to_text(self, text):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )

    def scroll_down(self):
        self.driver.swipe(start_x=500, start_y=1200, end_x=500, end_y=1000, duration=400)

    def wait_until_loading_disappear(self):
        self.wait.until(
            EC.invisibility_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Downloading Master Data")'
            ))
        )

    # actions
    def new_costumer_menu(self):
        self.wait_until_loading_disappear()
        self.wait.until(EC.presence_of_element_located(self.new_costumer_menu_xpath))
        self.wait.until(EC.element_to_be_clickable(self.new_costumer_menu_xpath)).click()

    def new_costumer_registration(self):
        self.wait.until(EC.element_to_be_clickable(self.new_costumer_registration_id)).click()

    def fill_basic_form(self):
        self.wait.until(EC.presence_of_element_located(self.outline_name_id)).send_keys(self.outline_name)
        self.wait.until(EC.presence_of_element_located(self.outline_phone_id)).send_keys(self.outline_phone)
        self.wait.until(EC.presence_of_element_located(self.outline_email_id)).send_keys(self.outline_email)
        self.wait.until(EC.presence_of_element_located(self.contact_person_id)).send_keys(self.contact_person)

        self.scroll_to_text("Pricelist")

        # channel dropdown
        self.wait.until(EC.element_to_be_clickable(self.channel_id)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_channel_xpath)).click()

        # costumer type dropdown
        self.wait.until(EC.presence_of_element_located(self.costumer_type_id))
        self.wait.until(EC.element_to_be_clickable(self.costumer_type_id)).click()

        self.wait.until(EC.presence_of_element_located(self.choose_costumer_xpath))
        self.wait.until(EC.element_to_be_clickable(self.choose_costumer_xpath)).click()

        # continue btn
        self.wait.until(EC.element_to_be_clickable(self.continue_btn_id)).click()

    def fill_location_form(self):
        # address type dropdown
        self.wait.until(EC.element_to_be_clickable(self.address_type_id)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_address_xpath)).click()

        self.wait.until(EC.presence_of_element_located(self.address_fill_id)).send_keys(self.address_fill)

        self.scroll_down()

        self.wait.until(EC.element_to_be_clickable(self.province_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_province_xpath)).click()

        self.scroll_to_text("Postal code*")

        self.wait.until(EC.element_to_be_clickable(self.city_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_city_xpath)).click()

        self.wait.until(EC.element_to_be_clickable(self.district_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_district_xpath)).click()

        self.wait.until(EC.element_to_be_clickable(self.subdistrict_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_subdistrict_xpath)).click()

        self.wait.until(EC.element_to_be_clickable(self.postal_code_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_postal_code_xpath)).click()

        # continue btn
        self.wait.until(EC.element_to_be_clickable(self.continue_btn_xpath)).click()

    def fill_documents_form(self):
        self.wait.until(EC.visibility_of_element_located(self.ktp_id)).send_keys(self.enter_ktp)
        self.wait.until(EC.element_to_be_clickable(self.upload_file_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.btn_capture_id)).click()
        self.wait.until(EC.element_to_be_clickable(self.submit_btn_xpath)).click()

    def approval_signature(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_here_id)).click()
        self.wait.until(EC.element_to_be_clickable(self.register_btn_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.dc_yes_xpath)).click()