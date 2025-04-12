import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    # Crea la carpeta evidencias/capturas si no existe
    os.makedirs("evidencias/capturas", exist_ok=True)

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_exitoso(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)

    # Captura antes del login
    driver.save_screenshot("evidencias/capturas/login_pantalla.png")

    # Realiza el login
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # Captura después del login
    driver.save_screenshot("evidencias/capturas/login_exitoso.png")

    # Validación final
    assert "dashboard" in driver.current_url
