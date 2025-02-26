from pages.basepage import BasePage
from pages.retrievelocators import RetrieveLocator
from resources.linkname import maxwait, insurancewebsite


class RetrieveQuotation(BasePage):
    def checkurl(self,driver):
        url1=self.currenturl(driver)

        if url1==insurancewebsite:
            self.navigateto(url1)
            print('right page')
        else:
            self.navigateto(insurancewebsite)

    def checkforquotationusingid(self):
        self.explicitlywaitelementclick(maxwait,RetrieveLocator.requestquotationbtn)
        file_data = RetrieveLocator.getfilecontents()
        print(file_data)
        if file_data:  # Ensure the file content is not empty
            self.findelement(RetrieveLocator.retrievefield, file_data)
            self.explicitlywaitelementclick(maxwait,RetrieveLocator.retrievebtn)
        else:
            print("No data found in sample.txt. Need to ")