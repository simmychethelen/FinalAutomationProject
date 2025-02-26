from selenium.webdriver.common.by import By
# This page contains the Locators for web elements in the Request for Quotation web page,
# and also a constant variable. This is passed in quotationpage3.

class QuotationLocator:
    requestquotationbtn=(By.XPATH,"//a[contains(text(),'Request')]")
    coverdd=(By.NAME,'0')
    covervalue='Roadside'
    radiorepair=(By.XPATH,"//input[@type='radio']")
    radiovalue='Yes'
    incidentfield=(By.XPATH,"//input[@name='incidents']")
    incidentvalue='Accident'
    registrationfeild=(By.XPATH,"//input[@name='registration']")
    registrationvalue='CAN235255'
    mileagefield=(By.XPATH,"//input[@name='mileage']")
    mileagevalue='130000'
    estimatefield = (By.XPATH, "//input[@name='value']")
    estimatevalue='85000'
    parkingdd=(By.XPATH, "//select[@name='parkinglocation']")
    parkingvalue='Locked Garage'
    policyyear=(By.NAME,"year")
    year='2023'
    policymonth = (By.NAME, "month")
    month = 'February'
    policydate = (By.NAME, "date")
    date = '7'
    calculatequotationbtn=(By.XPATH,"//*[@class='btn btn-default']")
    premium=(By.XPATH,"//p[@id='calculatedpremium']")
    savequote=(By.XPATH,"//*[@name='submit']")
    savepage=(By.XPATH,"/html/body")