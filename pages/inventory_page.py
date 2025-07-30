

from base.base_page import BasePage

from selenium.webdriver.common.by import By
 
class InventoryPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)
 
    def get_current_url(self):

        return self.driver.current_url
 
    def add_products_to_cart(self, count):

        add_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")

        for button in add_buttons[:count]:

            self.click(button)
 
    def click_cart_icon(self):

        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")

        self.click(cart_icon)

 