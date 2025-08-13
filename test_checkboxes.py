from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from checkboxes import Checkboxes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# Ruta al WebDriver (en este caso ChromeDriver)
service = Service("C:/webdriver/chromedriver.exe")
# Configuración de opciones del navegador
options = Options()
options.add_argument("--incognito")
# Inicia el navegador
driver = webdriver.Chrome(service=service, options=options)

# Abre la página de inicio de sesión
driver.get("https://the-internet.herokuapp.com/checkboxes")
# Espera un momento para que cargue la página
time.sleep(2)
# Crea una instancia de la página de inicio de sesión
test_checkboxes = Checkboxes(driver)
# Verifica el estado de las casillas de verificación
checkbox1 = test_checkboxes.check_checkbox1()
checkbox2 = test_checkboxes.check_checkbox2()
# Imprime el estado de las casillas de verificación
if checkbox1.is_selected():
    print("Checkbox 1 está seleccionado")
else:
    print("Checkbox 1 no está seleccionado")
if checkbox2.is_selected():
    print("Checkbox 2 está seleccionado")
else:
    print("Checkbox 2 no está seleccionado")