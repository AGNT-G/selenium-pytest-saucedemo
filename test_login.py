from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from login_page import LoginPage
# Ruta al WebDriver (en este caso ChromeDriver)
service = Service("C:/webdriver/chromedriver.exe")
# Inicia el navegador
driver = webdriver.Chrome(service=service)
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
time.sleep(2)
# Verifica el mensaje de éxito
success_message = login_page.get_success_message()
if "You logged into a secure area!" in success_message:
    print("Inicio de sesión exitoso")
else:
    print("Inicio de sesión fallido")   