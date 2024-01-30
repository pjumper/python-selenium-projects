from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class SigninPage(Page):
   EMAIL_FIELD = (By.ID, "username")
   PASSWORD_FIELD = (By.ID, "password")
   LOGIN_BUTTON = (By.ID, "login")
   INCORRECT_PASSWORD = (By.CSS_SELECTOR, "div.styles__AlertDisplayStyles-sc-vw2fsn-0.gieqYR div")


   def input_email(self, text, *locator):
       self.input_text(text, *self.EMAIL_FIELD)

   def incorrect_password_text(self, expected_text):
       actual_result = self.find_element(*self.INCORRECT_PASSWORD).text
       assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'

   def input_password(self, text, *locator):
       self.input_text(text, *self.PASSWORD_FIELD)

   def click_signin_button(self, *locator):
       self.click(*self.LOGIN_BUTTON)

