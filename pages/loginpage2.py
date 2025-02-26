from pages.basepage import BasePage
from pages.loginlocator import LoginLocator
from resources.linkname import maxwait,mainlink,scrollkey


class LoginPage(BasePage):

    def loginusernamepassword(self,userpass):
        self.findelementuserpass(LoginLocator.emailfield,userpass[0])
        self.findelementuserpass(LoginLocator.passwordfield, userpass[1])

    def submitafterlogin(self):
        self.explicitlywaitelementclick(maxwait,LoginLocator.sumbit)

    def checkurl(self,driver):
        url1=self.currenturl(driver)

        if url1==mainlink:
            self.navigateto(url1)
            print('You are in the Login Page')
        else:
            self.navigateto(mainlink)

    def successloginpage(self):
        successtext= self.getattributeofelement(maxwait,LoginLocator.loginsuccess).text
        if successtext==LoginLocator.welcomepage:
            print("Login successful")
            self.scrollpage(scrollkey)
        else:
            print("Unsuccessful Login")