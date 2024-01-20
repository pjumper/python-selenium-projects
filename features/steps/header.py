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


