from Pages.Home_page import HomePage
from Pages.Search_Results_Page import SearchResultsPage
from Pages.Product_page import ProductPage


def test_search_and_add_to_cart(driver):

    home = HomePage(driver)
    results = SearchResultsPage(driver)
    product = ProductPage(driver)

    # Search
    home.search_for("Selling Plans Ski Wax")

    # Click snowboard
    results.select_second_product()

    # Assert PDP
    assert "snowboard" in (
        product.get_title().lower()
    )

    # Add to cart
    product.add_to_cart()

    # Validate cart updated
    assert product.wait_for_cart_confirmation()