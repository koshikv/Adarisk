from selenium.webdriver.common.by import By


class Logins:
    inputbox_username_id = "user-name"
    inputbox_password_id = "password"
    button_login_xpath = '//input[@id="login-button"]'
    link_logout_linktext = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.inputbox_username_id).clear()
        self.driver.find_element(By.ID, self.inputbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.inputbox_password_id).clear()
        self.driver.find_element(By.ID, self.inputbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
