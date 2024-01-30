from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Input {email} in email field')
def input_email(context, email):
   context.app.signin_page.input_email(email)


@when('Input {password} in password field')
def input_password(context, password):
   context.app.signin_page.input_password(password)


@when('Click Signin button')
def click_signin_button(context):
   context.app.signin_page.click_signin_button()

@then('Verify {expected_text} is present')
def incorrect_password_text(context, expected_text):
   context.app.signin_page.incorrect_password_text(expected_text="We can't find your account.")




