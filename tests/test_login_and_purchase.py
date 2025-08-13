import pytest
from selenium import webdriver
from pages.login_page import Login_Page
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--incognito")  # Run in headless mode for CI/CD
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_login_and_purchase(driver):
    # Create instances of page objects
    login_page = Login_Page(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    # Log in to the application
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    # Add products to the cart
    products_page.add_two_products_to_cart()
    # Verify product names in the cart
    product1_name, product2_name = cart_page.check_product_names()
    assert product1_name == "Sauce Labs Backpack"
    assert product2_name == "Sauce Labs Bike Light"
    # Proceed to checkout
    cart_page.click_checkout()
    # Complete the purchase
    confirmation_message = checkout_page.complete_checkout("John", "Doe", "12345")
    # Verify order confirmation
    assert confirmation_message == "Thank you for your order!"
    # Optionally, you can add a print statement to confirm the test passed
    print("Test completed successfully: Purchase flow works as expected.")