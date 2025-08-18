from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from inputsandvalues import InputsAndValues
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta al WebDriver (en este caso ChromeDriver)
service = Service("C:/webdriver/chromedriver.exe")
# Configuración de opciones del navegador
options = Options()
options.add_argument("--incognito")
# Inicia el navegador
driver = webdriver.Chrome(service=service, options=options)
# Abre la página de entrada de valores
driver.get("https://the-internet.herokuapp.com/inputs")
# Espera un momento para que cargue la página
time.sleep(2)
# Crea una instancia de la clase InputsAndValues
test_inputs_andvalues = InputsAndValues(driver)
# Interactúa con el campo de entrada
input_element = test_inputs_andvalues.enter_value("12345")
# Ingresa un valor en el campo de entrada
test_inputs_andvalues.enter_value("67890")
# Obtiene el valor del campo de entrada
input_value = test_inputs_andvalues.get_value()
# Imprime el valor ingresado
print(f"El valor ingresado en el campo de entrada es: {input_value}")
# Cierra el navegador
driver.quit()