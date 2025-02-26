from pages.loginpage2 import LoginPage
from pages.quotationcheckpage3 import RequestQuotationCheck
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
        try:
            assert premiumamt!='',"Premium amount not calculated"
        except Exception as e:
            print("An error occurred: %s" % e)
        else:
            print("Premium amount calculated is with ", premiumamt)
            user1request.savequotation()
        finally:
            print("Test3 complete")

    #Test Case4 Clicking the request quotation tab and filling in details except vehicle value field  and clicking
    # calculating premium. A color change in the 'Estimated value' is seen which is asserted and unsuccessful
    #premium calculation is also asserted
    def test_checkfieldforempty(self,driver):
        user1check=RequestQuotationCheck(driver)
        user1check.checkurl(driver)
        user1check.checkforrequestquotationbtn()
        user1check.checkforvehiclevalue()
        checkpremium=user1check.unsuccessquotaionpage()
        try:
            assert checkpremium=='',"Premium is calculated"
        except Exception as e:
            print("An error occurred: %s" % e)
        else:
            print("The 'Estimated value' field cannot be empty. Values >100 premium will be calculated")
        finally:
            print("Testing completed")

    #Test Case5 Retriving the identification number from the txt file. Clicking the retrieve quotation and
    # entering the id number and clicking the retrieve button
    def test_sample(self,driver):
        user1request=RetrieveQuotation(driver)
        user1request.checkurl(driver)
        user1request.checkforquotationusingid()
        print("Test5 complete")
        time.sleep(3)
    print("Testing completed")

