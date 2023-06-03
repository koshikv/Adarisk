from PageObjects.LoginPage import Logins
from Utilities.ReadProperties import ReadConfig
from Utilities.Custom_logger import Logs


class Test_001_Login:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = Logs.genLogs()

    def test_login_000(self, setup):
        self.logger.info("********** test_login_000 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            print("test is passed....")
            self.logger.info("********** test_login_000 is passed **********")
            self.driver.close()
            assert True
        else:
            print("test is failed....")
            self.logger.error("********** test_login_000 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_000")
            self.driver.close()
            assert False

    def test_login_001(self, setup):
        self.logger.info("********** test_login_001 is started **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logi = Logins(self.driver)
        self.logi.setUserName(self.username)
        self.logi.setPassword(self.password)
        self.logi.clickLogin()
        self.act_title = self.driver.title
        if self.act_title == "Swag Labs":
            assert True
            print("test is passed.....")
            self.logger.info("********** test_login_001 is passed **********")
            self.driver.close()
        else:
            print("test is failed....")
            self.logger.info("********** test_login_001 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_001")
            self.driver.close()
            assert False
