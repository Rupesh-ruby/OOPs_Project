from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Justintime:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://justintime.in")

    def login(self):
        self.driver.find_element(By.XPATH, "//div[@class='custom-icon custom-customer']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
        self.driver.find_element(By.ID, "email").send_keys("rupe18ec105@rmkcet.ac.in")
        self.driver.find_element(By.ID, "pass").send_keys("Rupesh0412@")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign In']").click()

class AddWatch(Justintime):
    def order(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='New Arrivals']").click()
        self.driver.find_element(By.XPATH, "//*[@id='html-body']/div[4]/div[1]/div/div/div/div/div[3]/div[2]/div/a").click()
        self.driver.find_element(By.XPATH, "//span[text()='Checkout']")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Checkout']").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[6]").click()

    def Add_Address(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='New Arrivals']").click()
        self.driver.find_element(By.XPATH, "//*[@id='html-body']/div[4]/div[1]/div/div/div/div/div[3]/div[2]/div/a").click()
        self.driver.find_element(By.XPATH, "//span[text()='Checkout']")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Checkout']").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[6]").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[6]").send_keys("No:43/292 puz st")
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[7]").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[7]").send_keys("rajiji puram chennai")
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[10]").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[10]").send_keys("Vadodara")
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[11]").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[11]").send_keys("602001")
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[12]").click()
        self.driver.find_element(By.XPATH, "(//input[@class='input-text'])[12]").send_keys("9944504518")
        self.driver.find_element(By.XPATH, "//button[@class='button action continue primary']").click()

    def ele(self):
        try:
            self.driver.find_element(By.XPATH,"//div[@class='custom-icon custom-customer']").click()

        except:
            print("Invalid xpath")
obj = AddWatch()
while True:
    print("Enter 1 for login")
    print("Enter 2 for Add Items to bag if you are login")
    print("Enter 3 to add address if you are login")
    print("Enter 4 for clickToType")
    print("Enter 5 to exit")
    userchoice = int(input())
    if userchoice == 1:
        obj.login()
    elif userchoice==2:
        obj.order()
    elif userchoice ==3:
        obj.Add_Address()
    elif userchoice == 4:
        obj.ele()
    elif userchoice ==5:
        quit()