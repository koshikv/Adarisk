import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Logins
from Utilities.ReadProperties import ReadConfig
from Utilities.Custom_logger import Logs
from Utilities import XLUtils


class Test_002_Login_DDT:
    baseurl = ReadConfig.getApplicationUrl()
    file = ".//TestData//Testdata.xlsx"

    logger = Logs.genLogs()

    @pytest.mark.regression
    def test_002_Login_DDT_001(self, setup):
        self.logger.info("********** Test_002_Login_DDT_001 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 2, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 2, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 2, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.product_sort = self.driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
        if self.product_sort.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_001 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_001_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 2, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 2, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_001 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_001_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 2, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 2, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_002(self, setup):
        self.logger.info("********** Test_002_Login_DDT_002 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 3, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 3, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 3, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_002 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_002_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 3, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 3, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_002 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_002_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 3, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 3, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_003(self, setup):
        self.logger.info("********** test_002_Login_DDT_003 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 4, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 4, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 4, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.product_sort = self.driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
        if self.product_sort.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_003 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_003_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 4, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 4, 5, )
            self.driver.close()

        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_003 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_003_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 4, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 4, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_004(self, setup):
        self.logger.info("********** test_002_Login_DDT_004 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 5, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 5, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 5, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.product_sort = self.driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
        if self.product_sort.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_004 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_004_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 5, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 5, 5, )
            self.driver.close()

        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_004 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_004_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 5, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 5, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_005(self, setup):
        self.logger.info("********** Test_002_Login_DDT_005 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 6, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 6, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 6, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_005 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_005_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 6, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 6, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_005 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_005_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 6, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 6, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_006(self, setup):
        self.logger.info("********** Test_002_Login_DDT_006 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 7, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 7, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 7, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_006 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_006_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 7, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 7, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_006 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_006_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 7, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 7, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_007(self, setup):
        self.logger.info("********** Test_002_Login_DDT_007 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 8, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 8, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 8, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_007 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_007_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 8, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 8, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_007 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_007_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 8, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 8, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_008(self, setup):
        self.logger.info("********** Test_002_Login_DDT_008 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.password = XLUtils.readData(self.file, 'Sheet1', 9, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 9, 4)

        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(5)

        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_008 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_008_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 9, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 9, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_008 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_008_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 9, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 9, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_009(self, setup):
        self.logger.info("********** Test_002_Login_DDT_009 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 10, 2)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 10, 4)

        self.logi.setUserName(self.username)
        self.logi.clickLogin()
        time.sleep(5)

        self.error = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if self.error.is_displayed():
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_009 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_009_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 10, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 10, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_009 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_009_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 10, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 10, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_010(self, setup):
        self.logger.info("********** Test_002_Login_DDT_0010 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 11, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 11, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 11, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        time.sleep(5)

        self.pas = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        if self.pas.get_attribute('type') == 'password':
            assert True
            print("test is passed.....")
            self.logger.info("********** Test_002_Login_DDT_010 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_0010_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 11, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 11, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_010 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_010_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 11, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 11, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_012(self, setup):
        self.logger.info("********** Test_002_Login_DDT_0012 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 12, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 12, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 12, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(2)
        self.button_add_to_cart = self.driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        self.button_add_to_cart.click()
        self.num = self.driver.find_element(By.XPATH, "//*[text()='1']")
        if self.num.is_displayed():
            assert True
            print("test is passed...")
            self.logger.info("********** Test_002_Login_DDT_012 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_0012_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 12, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 12, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_012 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_012_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 12, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 12, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_013(self, setup):
        self.logger.info("********** Test_002_Login_DDT_0013 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 13, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 13, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 13, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        time.sleep(2)
        self.button_add_to_cart = self.driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        self.button_add_to_cart.click()
        self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_013_cart_before_remove.png")
        time.sleep(5)
        self.button_remove = self.driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
        self.button_remove.click()
        self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_013_cart_after_remove.png")

    @pytest.mark.regression
    def test_002_Login_DDT_014(self, setup):
        self.logger.info("********** Test_002_Login_DDT_0014 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 14, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 14, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 14, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.cart = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
        time.sleep(5)
        self.act_title = self.driver.title
        if self.act_title == 'Swag Labs':
            assert True
            print("test is passed...")
            self.logger.info("********** Test_002_Login_DDT_014 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_0014_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 14, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 14, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_014 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_014_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 14, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 14, 5, )
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_Login_DDT_015(self, setup):
        self.logger.info("********** Test_002_Login_DDT_0015 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)

        self.username = XLUtils.readData(self.file, 'Sheet1', 15, 2)
        self.password = XLUtils.readData(self.file, 'Sheet1', 15, 3)
        self.exp_result = XLUtils.readData(self.file, 'Sheet1', 15, 4)

        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        self.url = self.driver.current_url
        if self.url == "https://www.saucedemo.com/":
            assert True
            print("test is passed...")
            self.logger.info("********** Test_002_Login_DDT_015 is passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_0015_passed.png")
            XLUtils.writeData(self.file, 'Sheet1', 15, 5, 'Pass')
            XLUtils.fillGreenColor(self.file, 'Sheet1', 15, 5, )
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** Test_002_Login_DDT_015 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_002_Login_DDT_015_failed.png")
            XLUtils.writeData(self.file, 'Sheet1', 15, 5, 'Fail')
            XLUtils.fillRedColor(self.file, 'Sheet1', 15, 5, )
            self.driver.close()
            assert False
