from selenium.webdriver.common.by import By
class Checkboxes:
    def __init__(self, driver):
        self.driver = driver
        self.checkbox1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
        self.checkbox2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')
        


    # Métodos para interactuar con las casillas de verificación
    def check_checkbox1(self):
        checkbox1_element = self.driver.find_element(*self.checkbox1)
        if not checkbox1_element.is_selected():
            checkbox1_element.click()
        return checkbox1_element
    def check_checkbox2(self):
        checkbox2_element = self.driver.find_element(*self.checkbox2)
        if  checkbox2_element.is_selected():
            checkbox2_element.click()
        return checkbox2_element