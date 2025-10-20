import pytest
import openpyxl
from pages.data_driven import Data_Driven 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

def get_excel_data():
    wb = openpyxl.load_workbook('data/Sheet2.xlsx')
    sheet = wb['Hoja1']
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password, expected_result = row
        # Si las celdas están vacías, ignora esa fila
        if username is not None and password is not None and expected_result is not None:
            data.append((username, password, expected_result))
    return data

@pytest.mark.parametrize("username,password,expected_result", get_excel_data())
def test_login_ddt(username, password, expected_result):
    driver = webdriver.Chrome()  # O el navegador que uses
    driver.get("https://www.saucedemo.com/")
    login_page = Data_Driven(driver)
    login_page.login(username, password)

    if expected_result == "success":
        assert login_page.is_login_successful(), f"El login debería ser exitoso para {username}"
    elif expected_result == "fail":
        assert login_page.is_login_failed(), f"El login debería fallar para {username}"
    driver.quit()