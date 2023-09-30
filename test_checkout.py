
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_Creedence:

    def test_checkout(self):
        driver = webdriver.Edge()
        driver.get("https://automation.credence.in/login")
        driver.implicitly_wait(30)
        # login
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("bhushan01@test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Click on product1
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
        # add product into cart
        driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
        # click on proceed to checkout
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        # Enter Billing / shipping address
        # enter first name
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Bhushan")
        # enter last name
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Umbarkar")
        # enter phone
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("8381085898")
        # enter address
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Akola, Maharashtra")
        # enter zipcode
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("444101")
        # enter state
        state_select = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state_select.select_by_visible_text('Pune')

        # enter payment details
        # enter owner
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Bhushan")
        # enter card number
        # (This will not work we have to provide card number like a 4-4-4-4 digit)
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281037048916168")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        time.sleep(3)
        # enter CVV
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        time.sleep(3)
        # enter expiry year
        select_year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        time.sleep(3)
        select_year.select_by_visible_text("2023")
        time.sleep(2)
        # enter expiry month
        select_month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        select_month.select_by_index(2)
        time.sleep(2)
        # scroll down
        # scrl_dwn = driver.find_element(By.TAG_NAME, "html")
        # scrl_dwn.send_keys(Keys.END)

        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        time.sleep(3)
        print(driver.find_element(By.XPATH, "//p[@class='w-lg-50 mx-auto']").text)
        time.sleep(3)
        print(driver.find_element(By.XPATH, "//p[@class='lead w-lg-50 mx-auto']").text)
        time.sleep(3)
        print(driver.find_element(By.XPATH, "//h1[normalize-space()='Thank you.']").text)

        driver.close()


