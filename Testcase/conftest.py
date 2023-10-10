import pytest
from selenium.webdriver import Chrome
from time import sleep
@pytest.fixture
def launch():
    driver=Chrome("../Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("http://localhost/login.do")
    yield driver
    # driver.close()
