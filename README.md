# Selenium Automation Project

This project contains automated tests developed with **Python + Selenium**.  
The goal is to practice building automation frameworks following industry best practices.

## Technologies Used
- **Python 3**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Data-Driven Testing** (CSV/Excel)

## Project Structure
- `pages/` → Page classes (Page Object Model).
- `tests/` → Test cases with Pytest.
- `utils/` → Utilities and data handling (CSV/Excel).
- `conftest.py` → Pytest fixtures and configuration.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/AGNT-G/selenium-pytest-saucedemo.git

## Navigate to the project folder:

cd selenium-pytest-saucedemo


## Install dependencies:

pip install -r requirements.txt


## Run tests with Pytest:

pytest -v --html=report.html

## Example Test Flow

Open the login page.

## Enter valid/invalid credentials.

Validate success or error messages.

## Verify page redirection and UI elements.

This project demonstrates best practices in test automation with Python + Selenium, using a maintainable structure and reusable components.
