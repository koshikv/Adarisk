import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
        print("firefox browser is launching...")
    elif browser == "chrome":
        driver = webdriver.Chrome()
        print("chrome browser is running...")
    else:
        driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytestConfigur(config):
    config.metadata['Project Name'] = "Nop Commerce"
    config.metadata['Module Name'] = "Customers"
    config.metadata['tester'] = "koshik"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)