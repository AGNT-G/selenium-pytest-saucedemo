from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.input_username = (By.XPATH, '//*[@id="user-name"]')
        self.input_password = (By.XPATH, '//*[@id="password"]')
        self.button_login = (By.XPATH, '//*[@id="login-button"]')




    # Método para interactuar con el campo de entrada de usuario
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.input_username)
        ).send_keys(username)
    # Método para interactuar con el campo de entrada de contraseña
    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.input_password)
        ).send_keys(password)
    # Método para hacer clic en el botón de inicio de sesión
    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_login)
        ).click()