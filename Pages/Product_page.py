from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.Base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_TITLE = (
        By.TAG_NAME,
        "h1"
    )

    ADD_TO_CART_BTN = (
        By.XPATH,
        "//button[@name='add']"
    )

    CART_BADGE = (
        By.CSS_SELECTOR,
        ".cart-count-bubble"
    )

    def get_title(self):

        title = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_TITLE
            )
        )

        return title.text.strip()

    def add_to_cart(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.ADD_TO_CART_BTN
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def wait_for_cart_confirmation(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_BADGE
            )
        )

        badge = self.driver.find_element(
            *self.CART_BADGE
        )

        return badge.is_displayed()