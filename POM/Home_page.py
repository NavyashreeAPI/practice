from Generic.read_excel_file import *
loc=readfile("Home_page")
class Homepage:
    def __init__(self,driver):
        self.driver=driver
    def logout(self):
        self.driver.find_element(loc["logout"][0],loc["logout"][1]).click()

    def user_tab(self):
        self.driver.find_element(loc["user_tab"][0],loc["user_tab"][1]).click()

    def timetrack_tab(self):
        self.driver.find_element(loc["timetrack_tab"][0],loc["timetrack_tab"][1]).click()


