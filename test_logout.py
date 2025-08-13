from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from login_page import LoginPage
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
driver.get("https://the-internet.herokuapp.com/login")
# Espera un momento para que cargue la página
time.sleep(2)
# Crea una instancia de la página de inicio de sesión
login_page = LoginPage(driver)
# Ingresa el nombre de usuario y la contraseña
login_page.enter_username("tomsmith")
login_page.enter_password("SuperSecretPassword!")
time.sleep(2)
# Haz clic en el botón de inicio de sesión
login_page.click_login()
# Espera un momento para que se procese el inicio de sesión
wait = WebDriverWait(driver, 10)
wait.until(EC.url_to_be("https://the-internet.herokuapp.com/secure"))
# Verificar cambio de URL
if driver.current_url == "https://the-internet.herokuapp.com/secure":
    print("Cambio de URL exitoso")
else:
    print("Cambio de URL fallido")
# Verificar el botón de cierre de sesión
wait = WebDriverWait(driver, 10)
logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/logout']")))
print("Botón de cierre de sesión encontrado")
# Haz clic en el botón de cierre de sesión
login_page.click_logout()
# Espera un momento para que se procese el cierre de sesión
time.sleep(2)
# Verifica el mensaje de éxito
wait = WebDriverWait(driver, 10)
flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
success_message = flash.text

if "You logged out of the secure area!" in success_message:
    print("Cierre de sesión exitoso")
else:
    print("Cierre de sesión fallido")   