import time
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Logins
from Utilities.ReadProperties import ReadConfig
from Utilities import XLUtils
from Utilities.Custom_logger import Logs


class Test_003_Cart_DDT:
    baseurl = ReadConfig.getApplicationUrl()
    file = './/TestData//Testdata.xlsx'
    logger = Logs.genLogs()

    def test_003_cart_001(self, setup):
        self.logger.info('********** test_003_cart_001 is started **********')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, 'Sheet1', 2, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.act_url = self.driver.current_url
        if self.act_url == 'https://www.saucedemo.com/cart.html':
            assert True
            print("test case is passed...")
            self.logger.info('********** test_003_cart_001 is passed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_001_passed.png')
            self.driver.close()
        else:
            print('test case is failed...')
            self.logger.info('********** test_003_cart_001 is failed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_001_failed.png')
            self.driver.close()
            assert False

    def test_003_cart_002(self, setup):
        self.logger.info('********** test_003_cart_002 is started **********')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, 'Sheet1', 2, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        self.driver.back()
        time.sleep(2)
        self.act_url = self.driver.current_url
        if self.act_url == 'https://www.saucedemo.com/inventory.html':
            assert True
            print("test case is passed...")
            self.logger.info('********** test_003_cart_002 is passed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_002_passed.png')
            self.driver.close()
        else:
            print('test case is failed...')
            self.logger.info('********** test_003_cart_001 is failed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_002_failed.png')
            self.driver.close()
            assert False

    def test_003_cart_003(self, setup):
        self.logger.info('********** test_003_cart_003 is started **********')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, 'Sheet1', 2, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        time.sleep(2)
        self.button_cont_shopp = self.driver.find_element(By.XPATH, '//button[@id="continue-shopping"]').click()
        time.sleep(2)
        self.act_url = self.driver.current_url
        if self.act_url == 'https://www.saucedemo.com/inventory.html':
            assert True
            print("test case is passed...")
            self.logger.info('********** test_003_cart_002 is passed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_002_passed.png')
            self.driver.close()
        else:
            print('test case is failed...')
            self.logger.info('********** test_003_cart_001 is failed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_002_failed.png')
            self.driver.close()
            assert False

    def test_003_cart_004(self, setup):
        self.logger.info('********** test_003_cart_004 is started **********')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, 'Sheet1', 2, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        time.sleep(2)
        self.button_checkout = self.driver.find_element(By.XPATH, '//button[@name="checkout"]').click()
        time.sleep(2)
        self.act_url = self.driver.current_url
        if self.act_url == 'https://www.saucedemo.com/checkout-step-one.html':
            assert True
            print("test case is passed...")
            self.logger.info('********** test_003_cart_004 is passed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_004_passed.png')
            self.driver.close()
        else:
            print('test case is failed...')
            self.logger.info('********** test_003_cart_004 is failed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_004_failed.png')
            self.driver.close()
            assert False

    def test_003_cart_005(self, setup):
        self.logger.info('********** test_003_cart_005 is started **********')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.username = XLUtils.readData(self.file, 'Sheet1', 2, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 2, 3)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()

        self.items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
        for i in range(len(self.items)):
            self.driver.find_element(By.XPATH, '//button[contains(@id, "add-")]').click()
        time.sleep(5)
        self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_005.png')
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        time.sleep(5)
        self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_005.png')
        self.act_items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
        if len(self.items) == len(self.act_items):
            assert True
            print("test case is passed...")
            self.logger.info('********** test_003_cart_005 is passed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_005_passed.png')
            self.driver.close()
        else:
            print('test case is failed...')
            self.logger.info('********** test_003_cart_005 is failed **********')
            self.driver.save_screenshot('.//Screenshots//' + 'test_003_cart_005_failed.png')
            self.driver.close()
            assert False
