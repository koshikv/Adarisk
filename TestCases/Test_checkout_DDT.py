from selenium.webdriver.common.by import By
import time
from PageObjects.LoginPage import Logins
from Utilities.Custom_logger import Logs
from Utilities import XLUtils
from Utilities.ReadProperties import ReadConfig


class Test_004_Checkout_DDT:
    baseurl = ReadConfig.getApplicationUrl()
    file = ".//TestData/Testdata.xlsx"
    logger = Logs.genLogs()

    def test_004_Checkout_001(self, setup):
        self.logger.info("********** test_004_Checkout_001 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.act_url = self.driver.current_url
        if self.act_url == "https://www.saucedemo.com/checkout-step-one.html":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_001 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_001_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_001 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_001_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False

    def test_004_Checkout_002(self, setup):
        self.logger.info("********** test_004_Checkout_002 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').clear()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("rahul")
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').clear()
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("patil")
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').clear()
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(int('422009'))
        self.driver.find_element(By.XPATH, '//input[@name="continue"]').click()
        self.act_url = self.driver.current_url
        if self.act_url == "https://www.saucedemo.com/checkout-step-two.html":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_002 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_002_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_002 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_002_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False

    def test_004_Checkout_003(self, setup):
        self.logger.info("********** test_004_Checkout_003 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').clear()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("rahul")
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').clear()
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("patil")
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').clear()
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(int('422009'))
        self.driver.find_element(By.XPATH, '//input[@name="continue"]').click()
        self.driver.find_element(By.XPATH, '//button[@name="finish"]').click()
        self.act_url = self.driver.current_url
        if self.act_url == "https://www.saucedemo.com/checkout-complete.html":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_003 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_003_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_003 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_003_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False

    def test_004_Checkout_004(self, setup):
        self.logger.info("********** test_004_Checkout_004 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').clear()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("rahul")
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').clear()
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("patil")
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').clear()
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(int('422009'))
        self.driver.find_element(By.XPATH, '//input[@name="continue"]').click()
        self.driver.find_element(By.XPATH, '//button[@name="finish"]').click()
        self.driver.find_element(By.XPATH, '//button[@name="back-to-products"]').click()
        self.act_url = self.driver.current_url
        if self.act_url == "https://www.saucedemo.com/inventory.html":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_004 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_004_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_004 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_004_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False

    def test_004_Checkout_005(self, setup):
        self.logger.info("********** test_004_Checkout_005 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').clear()
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').clear()
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("patil")
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').clear()
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(int('422009'))
        self.driver.find_element(By.XPATH, '//input[@name="continue"]').click()
        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.text == "Error: First Name is required":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_005 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_005_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_005 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_005_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False

    def test_004_Checkout_006(self, setup):
        self.logger.info("********** test_004_Checkout_006 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').clear()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("rahul")
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').clear()
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').clear()
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(int('422009'))
        self.driver.find_element(By.XPATH, '//input[@name="continue"]').click()
        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.text == "Error: Last Name is required":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_006 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_006_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_006 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_006_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False

    def test_004_Checkout_007(self, setup):
        self.logger.info("********** test_004_Checkout_007 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, "Sheet1", 2, 2)
        self.password = XLUtils.readData(self.file, "Sheet1", 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').clear()
        self.f_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("rahul")
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').clear()
        self.l_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("patil")
        self.zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="continue"]').click()
        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.text == "Error: Postal Code is required":
            assert True
            print("test is passed...")
            self.logger.info("********** test_004_Checkout_007 is passed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_007_passed.png")
            time.sleep(2)
            self.driver.close()
        else:
            print("test is failed...")
            self.logger.info("********** test_004_Checkout_007 is failed **********")
            self.driver.save_screenshot(".//Screenshots//" + "test_004_Checkout_007_failed.png")
            time.sleep(2)
            self.driver.close()
            assert False
