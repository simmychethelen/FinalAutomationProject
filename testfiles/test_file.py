from pages.loginpage2 import LoginPage
from pages.quotationpage3 import RequestQuotation
from pages.registerformpage1 import RegisterPage
import time
from pages.retrievequotation4 import RetrieveQuotation


class Testcases:
    #Test Case 1 Going to the website, clicking Register button,pytest
    # Filling the signup as new userform
    def test_registeruser(self, driver, username_password):
        user1form=RegisterPage(driver)
        user1form.waitandselectdropdown()
        user1form.findelementuserpassandtype(username_password)
        user1form.submitbutnclick()
        user1form.pageattribute()
        print("Test1 complete")

        #time.sleep(10)
    # Test Case 2 Using the credentials created in test case1 trying Logging in successfully
    def test_login(self,driver,username_password):
        user1login=LoginPage(driver)
        user1login.checkurl(driver)
        user1login.loginusernamepassword(username_password)
        user1login.submitafterlogin()
        user1login.successloginpage()
        print("Test2 complete")

    #Test Case3 Clicking the request quotation tab and filling in details and calculating premium
    # and saving quotation and storing the unique identification number in a txt file and going back to the main page
    def test_quotaionrequest(self,driver):
        user1request=RequestQuotation(driver)
        user1request.checkurl(driver)
        user1request.checkforrequestquotationbtn()
        premiumamt=user1request.successquotaionpage()
        if premiumamt=='':
            print("Premium amount not calculated")
        else:
            print("Premium amount calculated is with ", premiumamt)
            user1request.savequotation()
        print("Test3 complete")

    #Test Case4 Retriving the identification number from the txt file. Clicking the retrieve quotation and
    # entering the id number and clicking the retrieve button
    def test_sample(self,driver):
        user1request=RetrieveQuotation(driver)
        user1request.checkurl(driver)
        user1request.checkforquotationusingid()
        print("Test4 complete")
        time.sleep(3)