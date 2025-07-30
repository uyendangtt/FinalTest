from base.base_page import BasePage
from selenium.webdriver.common.by import By
 
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = driver.find_element(By.ID, "user-name")
        self.password_input = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "login-button")
 
    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)