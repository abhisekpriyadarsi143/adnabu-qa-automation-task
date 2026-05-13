from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item, .cart__item")
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".cart-item__name, .cart__item-title")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".cart__empty-text, .is-empty")

    def get_cart_item_names(self) -> list:
        items = self.find_all(self.CART_ITEM_NAME)
        return [item.text.strip() for item in items]

    def is_cart_empty(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MSG)

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))