from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
   SIGNIN = (By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3")
   SIGNIN_MENU = (By.ID, "listaccountNav-signIn")
   SIGNED_IN_ICON = (By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3")
   VERIFY_HEADER_LINKS = (By.CSS_SELECTOR, "#headerPrimary .styles__DesktopLinkContainer-sc-8s5b77-4.bKvnJt")



   def click_signin(self, *locator):
       self.click(*self.SIGNIN)



   def click_signin_menu(self, *locator):
       self.click(*self.SIGNIN_MENU)

   def click_signed_in_icon(self, *locator):
       self.click(*self.SIGNED_IN_ICON)

   def verify_header_links(self, expected_amount, *locator):
       expected_amount = int(expected_amount)
       actual_amount = self.find_elements(*self.VERIFY_HEADER_LINKS)
       assert len(actual_amount) == expected_amount, f"Expected {expected_amount} but got {len(actual_amount)}"