from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    def open_home_page(self):
        self.open_url("https://www.target.com")