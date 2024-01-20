from pages.main_page import MainPage
from pages.header import Header
from pages.signin_page import SigninPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.signin_page = SigninPage(self.driver)

