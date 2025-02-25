from selenium.webdriver.support.select import Select
from pages.basepage import BasePage
from pages.registerlocator import RegisterLocator
from resources.linkname import maxwait, mainlink


class RegisterPage(BasePage):
    def waitandselectdropdown(self):
        self.navigateto(mainlink)
        self.explicitlywaitelementclick(maxwait,RegisterLocator.linktoregister)
        self.explicitlywaitelementdd(maxwait,RegisterLocator.title,RegisterLocator.titlename)
        self.findelement(RegisterLocator.firsttextfield,RegisterLocator.firstname)
        self.findelement(RegisterLocator.surnametextfield,RegisterLocator.surname)
        self.findelement(RegisterLocator.phonefield,RegisterLocator.phone)
        self.explicitlywaitelementdd(maxwait, RegisterLocator.yeardd, RegisterLocator.year)
        self.explicitlywaitelementdd(maxwait, RegisterLocator.monthdd, RegisterLocator.month)
        self.explicitlywaitelementdd(maxwait, RegisterLocator.daydd, RegisterLocator.date)
        radiobtn=self.findelements(RegisterLocator.radiobtn)
        for lb in radiobtn:
            v=lb.get_attribute('value')
            if v==RegisterLocator.radiovalue:
                lb.click()
                break
        self.explicitlywaitelementdd(maxwait, RegisterLocator.licenseperiod, RegisterLocator.period)
        self.explicitlywaitelementdd(maxwait, RegisterLocator.occupationdd, RegisterLocator.occupation)
        self.findelement(RegisterLocator.addressfield,RegisterLocator.address)
        self.findelement(RegisterLocator.cityfield,RegisterLocator.city)
        self.findelement(RegisterLocator.countryfield,RegisterLocator.country)
        self.findelement(RegisterLocator.postcodefield,RegisterLocator.postcode)

    def findelementuserpassandtype(self,userpass):
        self.findelementuserpass(RegisterLocator.emailfield,userpass[0])
        self.findelementuserpass(RegisterLocator.passwordfield, userpass[1])
        self.findelementuserpass(RegisterLocator.conpasswordfield, userpass[1])

    def submitbutnclick(self):
        self.explicitlywaitelementclick(maxwait,RegisterLocator.submitbtn)

    def pageattribute(self):
        txt1= self.getattributeofelement(maxwait,RegisterLocator.checkpage).text
        try:
            assert txt1=="Login","Not in Login Page"
            if txt1=="Login":
                print("Successfully entered the login page")
                # user1login=LoginPage(driver)
                # user1login.loginusernamepassword(username_password)
                # user1login.submitafterlogin()
        except Exception as e:
            print("An error occurred: %s" % e)
        else:
            print("The page is ",txt1,"page")
        finally:
            print("Testing completed")



