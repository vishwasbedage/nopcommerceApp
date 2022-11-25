from selenium import webdriver
import pytest


@pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):                  ## this will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")
#
#
# ############################# pytest html report ############################
## It is hook for adding enivroment info to html report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['tester'] = 'Vishwas Bedage'

## It is hook for delete/modify enivroment info to html report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)