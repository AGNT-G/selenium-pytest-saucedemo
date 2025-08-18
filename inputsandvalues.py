from selenium.webdriver.common.by import By
class InputsAndValues:
    def __init__(self, driver):
        self.driver = driver
        self.input = (By.XPATH, '//*[@id="content"]/div/div/div/input')
        




    # Método para interactuar con el campo de entrada
    def enter_value(self, value):
        input_element = self.driver.find_element(*self.input)
        input_element.clear()  # Limpia el campo antes de ingresar un nuevo valor
        input_element.send_keys(value)  # Ingresa el valor en el campo
        return input_element.get_attribute("value")  # Devuelve el valor ingresado en el campo de entrada

    # Método para obtener el valor del campo de entrada
    def get_value(self):
        input_element = self.driver.find_element(*self.input)
        return input_element.get_attribute("value")  # Obtiene el valor actual del campo de entrada
    