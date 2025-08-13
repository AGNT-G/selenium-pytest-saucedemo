from selenium.webdriver.common.by import By
class PracticeError:
    def __init__(self, driver):
        self.driver = driver
        self.input_email = (By.XPATH, '//*[@id="userEmail"]')
        self.input_submit = (By.XPATH, '//*[@id="submit"]')





    # Método para interactuar con el campo de entrada
    def enter_email(self, email):
        email_input = self.driver.find_element(*self.input_email)
        email_input.send_keys(email)
    def get_email_border_color(self):
        email_input = self.driver.find_element(*self.input_email)
        return email_input.value_of_css_property("border-color")
    def click_submit(self):
        submit_button = self.driver.find_element(*self.input_submit)
        submit_button.click()