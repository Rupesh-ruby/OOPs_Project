import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestJustintime:

    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver

    def test_login(self, driver):
        driver.get("https://justintime.in")
        driver.find_element(By.XPATH, "//div[@class='custom-icon custom-customer']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
        driver.find_element(By.ID, "email").send_keys("rupe18ec105@rmkcet.ac.in")
        driver.find_element(By.ID, "pass").send_keys("Rupesh0412@")
        driver.find_element(By.XPATH, "//span[normalize-space()='Sign In']").click()
        expected_header = 'New Arrivals'
        element = driver.find_element(By.XPATH,"//span[normalize-space()='New Arrivals']")
        element.click()
        element = driver.find_element(By.XPATH,"//span[contains(@class,'base')]")
        assert expected_header in element.text


