from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.Base_page import BasePage


class SearchResultsPage(BasePage):

    SECOND_PRODUCT = (
        By.XPATH,
        "//a[contains(@href,'the-complete-snowboard')]"
    )

    def select_second_product(self):

        product = self.wait.until(
            EC.presence_of_element_located(
                self.SECOND_PRODUCT
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            product
        )

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )