from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_product = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.second_product = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        self.cart_icon = (By.XPATH, '//*[@id="shopping_cart_container"]/a')


    # Método para agregar el primer producto al carrito
    def add_first_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_product)
        ).click()
    # Método para agregar el segundo producto al carrito
    def add_second_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.second_product)
        ).click()
    # Método para hacer clic en el icono del carrito
    def click_cart_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()
    def add_two_products_to_cart(self):
        self.add_first_product_to_cart()
        self.add_second_product_to_cart()
        self.click_cart_icon()