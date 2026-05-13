from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.Settings import EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def find_all(self, locator):
        self.find(locator)  # wait for at least one
        return self.driver.find_elements(*locator)