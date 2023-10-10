class Timetrack:
    def __init__(self,driver):
        self.driver=driver

    def user_select(self,user):
        self.driver.find_element(*loc["Timetrack"]["user_select"])
        self.driver.find_element("xpath", "//div[text()='user']")

    def new_tab(self):
        self.driver.find_element("xpath", "//a[.='New']").click()
        id=self.driver.window_handles
        self.driver.switch_to.window(id[1])

