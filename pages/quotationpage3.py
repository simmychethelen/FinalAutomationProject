from pages.basepage import BasePage
from pages.quotationlocator import QuotationLocator
from resources.linkname import insurancewebsite, maxwait


class RequestQuotation(BasePage):

    def checkurl(self,driver):
        url2=self.currenturl(driver)
        if url2==insurancewebsite:
            self.navigateto(url2)
            print('right page')
        else:
            self.navigateto(insurancewebsite)

    def checkforrequestquotationbtn(self):
        self.explicitlywaitelementclick(maxwait,QuotationLocator.requestquotationbtn)
        self.explicitlywaitelementdd(maxwait,QuotationLocator.coverdd,QuotationLocator.covervalue)
        radiobtn=self.findelements(QuotationLocator.radiorepair)
        for lb in radiobtn:
            v=lb.get_attribute('value')
            if v==QuotationLocator.radiovalue:
                lb.click()
                break
        self.findelement(QuotationLocator.incidentfield,QuotationLocator.incidentvalue)
        self.findelement(QuotationLocator.registrationfeild,QuotationLocator.registrationvalue)
        self.findelement(QuotationLocator.mileagefield,QuotationLocator.mileagevalue)
        self.findelement(QuotationLocator.estimatefield,QuotationLocator.estimatevalue)
        self.explicitlywaitelementdd(maxwait,QuotationLocator.parkingdd,QuotationLocator.parkingvalue)
        self.explicitlywaitelementdd(maxwait, QuotationLocator.policyyear, QuotationLocator.year)
        self.explicitlywaitelementdd(maxwait, QuotationLocator.policymonth, QuotationLocator.month)
        self.explicitlywaitelementdd(maxwait, QuotationLocator.policydate, QuotationLocator.date)
        self.explicitlywaitelementclick(maxwait,QuotationLocator.calculatequotationbtn)

    def successquotaionpage(self):
        return self.getattributeofelement(maxwait,QuotationLocator.premium).text
    def savequotation(self):
        self.explicitlywaitelementclick(maxwait,QuotationLocator.savequote)
        savequote=self.getattributeofelement(maxwait,QuotationLocator.savepage).text
        while savequote != '':
            digits=savequote.split(': ')
            digits1=digits[1].split('\n')
            number=str(digits1[0])
            fileA = open('Id.txt', 'w')
            fileA.write(number)
            fileA.close()
            self.gobacktomainpage()
            break
        return number