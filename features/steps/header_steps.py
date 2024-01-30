from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Signin')
def click_signin(context):
   context.app.header.click_signin()


@when('Click Signin Menu')
def click_signin_menu(context):
   context.app.header.click_signin_menu()

@when('Click Signed in icon')
def click_signed_in_icon(context):
   context.app.header.click_signed_in_icon()

@then('Verify {expected_amount} header links are present')
def verify_header_links(context, expected_amount):
   context.app.header.verify_header_links(expected_amount)
