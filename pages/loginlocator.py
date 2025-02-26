from selenium.webdriver.common.by import By

# This page contains the Locators for web elements in the login web page
# and also a constant variable. These are called in loginpage2
class LoginLocator:
    emailfield=(By.NAME,"email")
    passwordfield=(By.NAME,"password")
    sumbit=(By.NAME,"submit")
    loginsuccess=(By.XPATH,"// *[text() = 'Broker Insurance WebPage'] // parent::div")
    welcomepage='Broker Insurance WebPage'