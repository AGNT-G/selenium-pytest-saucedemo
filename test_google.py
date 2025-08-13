from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Ruta al WebDriver (en este caso ChromeDriver)
service = Service("C:/webdriver/chromedriver.exe")  

# Inicia el navegador
driver = webdriver.Chrome(service=service)

# Abre Google
driver.get("https://the-internet.herokuapp.com/login")

# Espera un momento para que cargue la página
time.sleep(2)

username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button')
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login_button.click()
success_message = driver.find_element(By.XPATH, '//*[@id="flash"]')
# Espera un momento para que se procese el inicio de sesión
if "You logged into a secure area!" in success_message.text:
    print("Inicio de sesión exitoso")
else:
    print("Inicio de sesión fallido")
time.sleep(2)
# Cierra el navegador
driver.quit()
