class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
 
    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.enter_text(self.driver.find_element(By.ID, "first-name"), first_name)
        self.enter_text(self.driver.find_element(By.ID, "last-name"), last_name)
        self.enter_text(self.driver.find_element(By.ID, "postal-code"), postal_code)
        self.click(self.driver.find_element(By.ID, "continue"))
 
    def complete_checkout(self):
        self.click(self.driver.find_element(By.ID, "finish"))
 
    def get_confirmation_messages(self):
        messages = []
        messages.append(self.driver.find_element(By.CLASS_NAME, "complete-header").text)
        messages.append(self.driver.find_element(By.CLASS_NAME, "complete-text").text)
        return messages