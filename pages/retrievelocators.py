from selenium.webdriver.common.by import By
# This page contains the Locators for web elements in the Retrieve quotation web page,
# and also a stores the Id in a text file id.txt. This is passed in retrievequotation4 page.

class RetrieveLocator:
    requestquotationbtn=(By.XPATH,"//*[@id='ui-id-3']")
    retrievefield=(By.XPATH,"// *[ @ name = 'id']")
    retrievebtn=(By.ID,"getquote")
    def getfilecontents():
        try:
            with open('Id.txt', 'r') as fileA:
                return fileA.read()
        except FileNotFoundError:
            print("Error: sample.txt file not found.")
            return ""
        except Exception as e:
            print(f"Error reading the file: {e}")
            return ""