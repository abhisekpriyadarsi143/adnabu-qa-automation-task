import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.Settings import (
    BASE_URL,
    STORE_PASSWORD,
    IMPLICIT_WAIT
)


@pytest.fixture(scope="function")
def driver():

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(IMPLICIT_WAIT)

    driver.get(BASE_URL)

    handle_store_password(driver)

    yield driver

    driver.quit()


def handle_store_password(driver):

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        wait = WebDriverWait(driver, 5)

        password_input = wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        password_input.send_keys(STORE_PASSWORD)

        driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()
        driver.refresh()

    except Exception:
        pass