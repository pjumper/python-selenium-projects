from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains

class AccountMenu(Page):

    CLICK_ACCOUNT_LINK = (By.CSS_SELECTOR, "[href='/account?lnk=acct_nav_my_account']")
    VERIFY_SIGN_OUT_LINK = (By.XPATH, "//a[@data-test='accountNav-guestSignOut']")
    VERIFY_ACCOUNT_PAGE_OPENED = (By.XPATH, "//div[@class='styles__StyledRow-sc-wmoju4-0 jJAWfL'] [h2]")
    VERIFY_ACCOUNT_LINKS = (By.CSS_SELECTOR, '.styles__PageGrid-sc-1civ2nm-4 .styles__CardWrapper-sc-dkpfky-0')

    def click_account_link(self, *locator):
        self.click(*self.CLICK_ACCOUNT_LINK)


    def verify_sign_out_link(self, *locator):
        sign_out = self.wait_for_element_appear(*self.VERIFY_SIGN_OUT_LINK)
        assert sign_out, f'sign out is not displayed'


    def verify_account_page_opened(self, expected_text, *locator):
        actual_result = self.find_element(*self.VERIFY_ACCOUNT_PAGE_OPENED).text
        assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'

    def verify_account_menu_links(self, expected_count, *locator):
        expected_count = int(expected_count)
        actual_count = self.find_elements(*self.VERIFY_ACCOUNT_LINKS)
        length_count = len(actual_count)
        actual_result = int(length_count) + 1
        assert actual_result == expected_count, f'Expected {expected_count}, but got {actual_result}'