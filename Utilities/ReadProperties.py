import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common_info", "baseurl")
        return url

    @staticmethod
    def getUserName():
        username = config.get("common_info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common_info", "password")
        return password
