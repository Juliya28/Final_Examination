import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import requests


with open("./testdata.yaml") as f:
   testdata = yaml.safe_load(f)
   
name = testdata["username"]
# passwd = testdata['password']

@pytest.fixture()
def er1():
   return "401"

@pytest.fixture()
def er2():
   return "Hello, {}".format(name)


@pytest.fixture(scope="session")
def browser():
    # if browser == "firefox":
    #     service = Service(executable_path=GeckoDriverManager().install())
    #     options = webdriver.FirefoxOptions()
    #     driver = webdriver.Firefox(service=service, options=options)
    # elif browser == "chrome":
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def about_page():
    return 'About Page'


@pytest.fixture()
def font_size():
    return '32px'