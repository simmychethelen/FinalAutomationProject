from selenium.webdriver.common.by import By


class LoginLocator:
    emailfield=(By.NAME,"email")
    passwordfield=(By.NAME,"password")
    sumbit=(By.NAME,"submit")
    loginsuccess=(By.XPATH,"// *[text() = 'Broker Insurance WebPage'] // parent::div")
    welcomepage='Broker Insurance WebPage'