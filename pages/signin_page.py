from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class SigninPage(Page):
   EMAIL_FIELD = (By.ID, "username")
   PASSWORD_FIELD = (By.ID, "password")


   def input_email(self, text, *locator):
       self.input_text(text, *self.EMAIL_FIELD)


   def input_password(self, text, *locator):
       self.input_text(text, *self.PASSWORD_FIELD)
