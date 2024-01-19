from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Home Page')
def open_home_page(context):
    context.app.main_page.open_home_page()

