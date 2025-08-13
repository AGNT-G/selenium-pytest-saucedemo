
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.practice_error import PracticeError
def test_practice_error():

    
    # Ruta al WebDriver (en este caso ChromeDriver)
    service = Service("C:/webdriver/chromedriver.exe")
    # Inicia el navegador
    driver = webdriver.Chrome(service=service)
    # Pantalla completa
    driver.maximize_window()
    # Abre la página de inicio de sesión
    driver.get("https://demoqa.com/automation-practice-form")
    # Espera un momento para que cargue la página
    wait = WebDriverWait(driver, 10)
    # Crea una instancia de la clase PracticeError
    practice_error_page = PracticeError(driver)
    # Interactúa con el campo de entrada de correo electrónico
    practice_error_page.enter_email("invalid-email-format")
    # Clica en el botón de enviar
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Espera un momento para que se procese el scroll
    practice_error_page.click_submit()
    # Espera un momento para que se procese la entrada
    time.sleep(1)
    # Clica en el botón de enviar
    practice_error_page.click_submit()
    # Espera un momento para que se procese la entrada
    wait = WebDriverWait(driver, 5)
    # Obtiene el color del borde del campo de entrada
    border_color = practice_error_page.get_email_border_color()
    # Imprime el color del borde
    print("Border color of the email input:", border_color)
    # Cierra el navegador
    driver.quit()
    # Espera un momento para que se procese la entrada
    time.sleep(1) 






    # Verifica que el color del borde sea rojo
    assert border_color == "rgb(220, 53, 69)", f"Expected red border color, but got {border_color}"
    print("Test passed: The email input field has a red border as expected.")




def test_valid_email_not_red_border():
    # Ruta al WebDriver (en este caso ChromeDriver)
    service = Service("C:/webdriver/chromedriver.exe")
    # Inicia el navegador
    driver = webdriver.Chrome(service=service)
    # Abre la página de inicio de sesión
    driver.get("https://demoqa.com/automation-practice-form")
    # Espera un momento para que cargue la página
    wait = WebDriverWait(driver, 10)
    # Crea una instancia de la clase PracticeError
    practice_error_page = PracticeError(driver)
    # Interactúa con el campo de entrada de correo electrónico
    practice_error_page.enter_email("correo@ejemplo.com")
    # Clica en el botón de enviar
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    # Espera un momento para que se procese el scroll
    practice_error_page.click_submit()
    # Espera un momento para que se procese la entrada
    time.sleep(1)
    # Espera un momento para que se procese la entrada
    wait = WebDriverWait(driver, 5)
    # Obtiene el color del borde del campo de entrada
    border_color = practice_error_page.get_email_border_color()
    # Imprime el color del borde
    print("Border color of the email input:", border_color)
    # Cierra el navegador
    driver.quit()
    # Espera un momento para que se procese la entrada
    time.sleep(1)

    # Verifica que el color del borde no sea rojo
    assert border_color != "rgb(220, 53, 69)", f"Expected non-red border color, but got {border_color}"
    print("Test passed: The email input field does not have a red border as expected for a valid email.")

