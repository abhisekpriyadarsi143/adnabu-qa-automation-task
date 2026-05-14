from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from Pages.Base_page import BasePage


class HomePage(BasePage):

    SEARCH_ICON = (
        By.CSS_SELECTOR,
        "summary[aria-label='Search'], button[aria-label='Search']"
    )

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[type='search']"
    )

    def search_for(self, product_name):

        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_ICON)
        ).click()

        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)