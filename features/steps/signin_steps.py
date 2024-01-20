from selenium.webdriver.common.by import By
from behave import given, when, then




@when('Input {email} in email field')
def input_email(context, email):
   context.app.signin_page.input_email(email)


@when('Input {password} in password field')
def input_password(context, password):
   context.app.signin_page.input_password(password)




