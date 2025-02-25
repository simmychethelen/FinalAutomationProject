from selenium.webdriver.common.by import By

class RegisterLocator:
    linktoregister=(By.XPATH,"//a[text()='Register']")
    title = (By.ID, "user_title")
    firsttextfield = (By.ID, "user_firstname")
    surnametextfield=(By.ID,"user_surname")
    phonefield=(By.ID,"user_phone")
    yeardd=(By.ID,"user_dateofbirth_1i")
    monthdd=(By.XPATH,'//*[@id="user_dateofbirth_2i"]')
    daydd=(By.CSS_SELECTOR,"select[name=date]")
    radiobtn=(By.XPATH,"//input[@type='radio']")
    licenseperiod=(By.ID,"user_licenceperiod")
    occupationdd=(By.ID,"user_occupation_id")
    addressfield=(By.ID,"user_address_attributes_street")
    cityfield=(By.ID,"user_address_attributes_city")
    countryfield=(By.ID,"user_address_attributes_county")
    postcodefield=(By.NAME,"post_code")
    emailfield=(By.NAME,"email")
    passwordfield=(By.NAME,"password")
    conpasswordfield=(By.NAME,"c_password")
    submitbtn=(By.XPATH,"//*[@type='submit']")
    checkpage=(By.XPATH,"//h3")
    titlename = 'Mrs'
    firstname = 'Mary'
    surname = 'Ben'
    phone = '123-456-789'
    year = '1988'
    month = 'April'
    date='25'
    radiovalue='Provisional'
    period='5'
    occupation='Doctor'
    address='3, college street'
    city='Toronto'
    country='Canada'
    postcode='A2B3C4'


