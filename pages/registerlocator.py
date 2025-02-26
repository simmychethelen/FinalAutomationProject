from selenium.webdriver.common.by import By
# This page contains the Locators for web elements in the Sign-up as new user(Register) web page,
# and also a constant variable. This is passed in registerformpage1.

class RegisterLocator:
    linktoregister=(By.XPATH,"//a[text()='Register']")
    title = (By.ID, "user_title")
    titlename = 'Mrs'
    firsttextfield = (By.ID, "user_firstname")
    firstname = 'Mary'
    surnametextfield=(By.ID,"user_surname")
    surname = 'Ben'
    phonefield=(By.ID,"user_phone")
    phone = '123-456-789'
    yeardd=(By.ID,"user_dateofbirth_1i")
    year = '1988'
    monthdd=(By.XPATH,'//*[@id="user_dateofbirth_2i"]')
    month = 'April'
    daydd=(By.CSS_SELECTOR,"select[name=date]")
    date='25'
    radiobtn=(By.XPATH,"//input[@type='radio']")
    radiovalue = 'Provisional'
    licenseperiod=(By.ID,"user_licenceperiod")
    period = '5'
    occupationdd=(By.ID,"user_occupation_id")
    occupation = 'Doctor'
    addressfield=(By.ID,"user_address_attributes_street")
    address = '3, college street'
    cityfield=(By.ID,"user_address_attributes_city")
    city = 'Toronto'
    countryfield=(By.ID,"user_address_attributes_county")
    country = 'Canada'
    postcodefield=(By.NAME,"post_code")
    postcode = 'A2B3C4'
    emailfield=(By.NAME,"email")
    passwordfield=(By.NAME,"password")
    conpasswordfield=(By.NAME,"c_password")
    submitbtn=(By.XPATH,"//*[@type='submit']")
    checkpage=(By.XPATH,"//h3")