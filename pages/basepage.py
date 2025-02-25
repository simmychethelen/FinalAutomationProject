from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.number=0

    def navigateto(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def explicitlywaitelementclick(self, interval, storelocate):
        WebDriverWait(self.driver, interval).until(ec.presence_of_element_located(storelocate)).click()

    def explicitlywaitelementdd(self, interval, storelocate,text1):
        waitlook=Select(WebDriverWait(self.driver, interval).until(ec.presence_of_element_located(storelocate)))
        waitlook.select_by_visible_text(text1)

    def findelementuserpass(self, storelocate,username):
        self.driver.find_element(*storelocate).send_keys(username)

    def findelement(self,firstname,text1):
        return self.driver.find_element(*firstname).send_keys(text1)

    def findelements(self,firstname):
        return self.driver.find_elements(*firstname)

    def getattributeofelement(self,interval,locate1):
        return WebDriverWait(self.driver, interval).until(ec.presence_of_element_located(locate1))

    def currenturl(self,driver):
        currenturl1 = self.driver.current_url
        return currenturl1

    def scrollpage(self,scrolling):
        self.driver.execute_script(scrolling)

    def gobacktomainpage(self):
        self.driver.back()