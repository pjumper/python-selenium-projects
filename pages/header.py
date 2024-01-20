from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
   SIGNIN = (By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3")
   SIGNIN_MENU = (By.ID, "listaccountNav-signIn")
   SIGNED_IN_ICON = (By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3")




   def click_signin(self, *locator):
       self.click(*self.SIGNIN)



   def click_signin_menu(self, *locator):
       self.click(*self.SIGNIN_MENU)

   def click_signed_in_icon(self, *locator):
       self.click(*self.SIGNED_IN_ICON)