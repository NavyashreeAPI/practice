from Generic.screenshot import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def verify(driver,title):
    wait=WebDriverWait(driver,10)
    try:
        wait.until(EC.title_is(title))
    except:
        take_screenshot(driver)
        raise Exception


