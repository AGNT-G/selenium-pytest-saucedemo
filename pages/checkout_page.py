from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.XPATH, '//*[@id="first-name"]')
        self.last_name_field = (By.XPATH, '//*[@id="last-name"]')
        self.zip_code_field = (By.XPATH, '//*[@id="postal-code"]')
        self.continue_button = (By.XPATH, '//*[@id="continue"]')
        self.finish_button = (By.XPATH, '//*[@id="finish"]')
        self.order_confirmation_message = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')




# Métodos para interactuar con la página de checkout
    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_field)
        ).send_keys(first_name) 
    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.last_name_field)
        ).send_keys(last_name)
    def enter_zip_code(self, zip_code):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.zip_code_field)
        ).send_keys(zip_code)
    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
    def get_order_confirmation_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.order_confirmation_message)
        ).text
    # Método para completar el proceso de checkout
    def complete_checkout(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.click_continue()
        self.click_finish()
        return self.get_order_confirmation_message()