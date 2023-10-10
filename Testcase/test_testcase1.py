from Generic.verfication import *
from POM.Home_page import Homepage
from POM.Login_PAge import Login_PAge


def test_testcase1(launch):
    driver=launch
    verify(driver,"actiTIME - Login")
    l=Login_PAge(driver)
    l.Username("admin")
    l.password("manager")
    l.login_button()
    verify(driver,"actiTIME - Enter Time-Track")
    h=Homepage(driver)
    h.logout()
    verify(driver,"actiTIME - Login")



