import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from inputsandvalues import InputsAndValues
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
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
    yield driver
    # Cierra el navegador después de las pruebas
    driver.quit()


def test_input_positive_number(driver):
    page = InputsAndValues(driver)
    result = page.enter_value(123)
    assert result == "123"

def test_input_negative_number(driver):
    page = InputsAndValues(driver)
    result = page.enter_value(-456)
    assert result == "-456"



    