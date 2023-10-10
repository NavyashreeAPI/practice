from Generic.verfication import *
from POM.Home_page import Homepage
from POM.Login_PAge import Login_PAge
from POM.USer_list_page import USerlistPage


def test_testcase2(launch):
    driver=launch
    verify(driver,"actiTIME - Login")
    l=Login_PAge(driver)
    l.Username("admin")
    l.password("manager")
    l.login_button()
    verify(driver,"actiTIME - Enter Time-Track")
    h=Homepage(driver)
    h.user_tab()
    u=USerlistPage(driver)
    u.user_button()
    u.firstname("Navya")
    u.lastname("shree")
    u.emailid("Navyashree694@gmail.com")
    u.username("navyapinky")
    u.password("Summer90*")
    u.retype_password("Summer90*")
    u.create_user()


