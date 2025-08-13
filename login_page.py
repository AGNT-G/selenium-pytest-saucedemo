from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, '//*[@id="username"]')
        self.password_field = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH, '//*[@id="login"]/button')
        self.success_message = (By.XPATH, '//*[@id="flash"]')
        self.logout_button = (By.XPATH, '//*[@id="content"]/div/a/i')

          

    # Métodos para interactuar con la página de inicio de sesión
    def enter_username(self, username):
        username_input = self.driver.find_element(*self.username_field)
        username_input.send_keys(username)
    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_field)
        password_input.send_keys(password)
    def click_login(self):
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
    def get_success_message(self):
        success_msg = self.driver.find_element(*self.success_message)
        return success_msg.text if success_msg else None
    def click_logout(self):
        logout_btn = self.driver.find_element(*self.logout_button)
        logout_btn.click()