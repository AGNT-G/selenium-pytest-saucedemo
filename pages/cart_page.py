from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.product1 = (By.XPATH, '//*[@id="item_4_title_link"]/div')
        self.product2 = (By.XPATH, '//*[@id="item_0_title_link"]/div')
        self.checkout_button = (By.XPATH, '//*[@id="checkout"]')

    def get_product_name(self, product_locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(product_locator)
        ).text
    
    def check_product_names(self):
        product1_name = self.get_product_name(self.product1)
        product2_name = self.get_product_name(self.product2)
        return product1_name, product2_name
    
    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()