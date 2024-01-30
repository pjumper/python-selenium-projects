from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    VERIFY_FOOTER_LINKS = (By.CSS_SELECTOR, "div .styles__StyledLink-sc-vpsldm-0.styles__StyledLink-sc-vbvkc1-9.cnZxgy.ROwZp")

    def open_home_page(self):
        self.open_url("https://www.target.com")

    def verify_footer_links(self, expected_count, *locator):
        expected_count = int(expected_count)
        actual_count = self.find_elements(*self.VERIFY_FOOTER_LINKS)
        length_link = len(actual_count)
        actual_result = int(length_link)
        assert actual_result == expected_count, f"Expected {expected_count} but got {actual_result}"

