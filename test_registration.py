
# import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Test_Credenece:

    def test_registration(self):
        # 1. open Browser
        driver = webdriver.Edge()
        # 2. Go to URL and # 3. Click Register link
        driver.get("https://automation.credence.in/register")
        driver.implicitly_wait(50)
        # 4. Enter Name
        driver.find_element(By.ID, "name").send_keys("Credence")
        # 5. Enter Email
        driver.find_element(By.ID, "email").send_keys("bhushan01@1test.com")
        # 6. Enter Password
        driver.find_element(By.NAME, "password").send_keys("Credence@1234")
        # 7. Enter Confirm Password
        driver.find_element(By.ID, "password-confirm").send_keys("Credence@1234")
        # 8. Click Register Button
        driver.find_element(By.CLASS_NAME, "btn").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            driver.close()
            assert True
            print("Registration TestCase is Passed !")
        except NoSuchElementException:
            print("Registration TestCase is Failed !")
            driver.close()
            assert False



