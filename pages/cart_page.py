from base.base_page import BasePage
from selenium.webdriver.common.by import By
 
class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = driver.find_element(By.ID, "checkout")
 
    def click_checkout(self):
        self.click(self.checkout_button)