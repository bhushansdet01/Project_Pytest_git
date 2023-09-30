from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Test_Creden:

    def test_login_001(self):
        # # 1. open browser
        driver = webdriver.Edge()
        # # 2. goto url
        driver.get("https://automation.credence.in/login")
        # time.sleep(5)
        driver.implicitly_wait(100)
        # # 3. Enter Email Address
        driver.find_element(By.ID, "email").send_keys("bhushan01@test.com")
        # time.sleep(5)
        # # 4. Enter Password
        driver.find_element(By.ID, "password").send_keys("Credence@123")
        # time.sleep(5)
        # # 5. click login button
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        # time.sleep(2)
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed..")
            driver.close()
            assert True

        except:
            print("Login TestCase is Failed..")
            driver.close()
            assert False










