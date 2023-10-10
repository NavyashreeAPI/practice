from Generic.read_excel_file import *
# loc=readfile("Login")

from Generic.reading_Json import *
loc=read_json_locator()
class Login_PAge:
    def __init__(self,driver):
        self.driver=driver
    def Username(self,data):
        self.driver.find_element(*loc["Login_PAge"]["Username"]).send_keys(data)

    def password(self,data):
        self.driver.find_element(*loc["Login_PAge"]["password"]).send_keys(data)

    def login_button(self):
        self.driver.find_element(*loc["Login_PAge"]["login_button"]).click()

