import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base.base_test import setup

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import BASE_URL

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_successful_login(self):
        self.driver.get(BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)
        assert "inventory" in inventory_page.get_current_url()