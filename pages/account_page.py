from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains

class AccountPage(Page):

    VERIFY_ACCOUNT_LINKS = (By.CSS_SELECTOR, '.styles__PageGrid-sc-1civ2nm-4 .styles__CardWrapper-sc-dkpfky-0')