from pages.basepage import BasePage
from pages.quotationlocator import QuotationLocator
from resources.linkname import insurancewebsite, maxwait


class RequestQuotationCheck(BasePage):

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
        self.findelement(QuotationLocator.estimatefield,QuotationLocator.estimatevalue1)
        self.explicitlywaitelementdd(maxwait,QuotationLocator.parkingdd,QuotationLocator.parkingvalue)
        self.explicitlywaitelementdd(maxwait, QuotationLocator.policyyear, QuotationLocator.year)
        self.explicitlywaitelementdd(maxwait, QuotationLocator.policymonth, QuotationLocator.month)
        self.explicitlywaitelementdd(maxwait, QuotationLocator.policydate, QuotationLocator.date)

    def checkforvehiclevalue(self):
        self.explicitlywaitelementclick(maxwait,QuotationLocator.calculatequotationbtn)
        checkfield=self.getattributeofelement(maxwait,QuotationLocator.checkestimatevalue)
        fieldcolor=checkfield.value_of_css_property('background-color')
        assert fieldcolor == 'rgba(255, 255, 153, 1)' or 'rgb(255, 255, 154)', "Color is not yellow. Field not empty"

    def unsuccessquotaionpage(self):
        return self.getattributeofelement(maxwait,QuotationLocator.premium).text