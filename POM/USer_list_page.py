
from Generic.read_excel_file import *
loc=readfile("USer_list")
class USerlistPage:
    def __init__(self,driver):
        self.driver=driver
    def user_button(self):
        self.driver.find_element(loc["user_button"][0],loc["user_button"][1]).click()

    def firstname(self,data):
        self.driver.find_element(loc["firstname"][0],loc["firstname"][1]).send_keys(data)

    def lastname(self, data):
        self.driver.find_element(loc["lastname"][0],loc["lastname"][1]).send_keys(data)

    def emailid(self, data):
        self.driver.find_element(loc["emailid"][0],loc["emailid"][1]).send_keys(data)

    def username(self,data):
        self.driver.find_element(loc["username"][0],loc["username"][1]).send_keys(data)

    def password(self,data):
        self.driver.find_element(loc["password"][0],loc["password"][1]).send_keys(data)

    def retype_password(self,data):
        self.driver.find_element(loc["retype_password"][0],loc["retype_password"][1]).send_keys(data)

    def create_user(self):
        self.driver.find_element(loc["create_user"][0],loc["create_user"][1]).click()

