import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base.base_test import setup

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import BASE_URL
from utils.config_reader import BASE_USERNAME
from utils.config_reader import BASE_PASSWORD



@pytest.mark.usefixtures("setup")

class TestCheckout:
    def test_add_products_and_checkout(self):
        self.driver.get(BASE_URL)
        LoginPage(self.driver).login(BASE_USERNAME, BASE_PASSWORD)
        inventory_page = InventoryPage(self.driver)

        inventory_page.add_products_to_cart(3)
        inventory_page.click_cart_icon()
        CartPage(self.driver).click_checkout()
        checkout_page = CheckoutPage(self.driver)
        
        checkout_page.enter_checkout_info("John", "Doe", "70000")
        checkout_page.complete_checkout()
        messages = checkout_page.get_confirmation_messages()
        assert "Thank you for your order!" in messages
        assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in messages

 