

from selenium.webdriver.support.select import Select
class CreateNewTask:
    def __init__(self,driver):
        self.driver=driver

    def select_customer(self):
        elem= self.driver.find_element("xpath","//select[@name='customerId']")
        s=Select(elem)
        s.select_by_value("-2")
    def enter_customer_name(self,data):
        self.driver.find_element("xpath", "//input[@name='customerName']").send_keys(data)

    def enter_project_name(self,data):
        self.driver.find_element("xpath", "//input[@name='projectName']").send_keys(data)

    def enter_task(self, data):
        self.driver.find_element("xpath", "//input[@id='task[0].name']").send_keys(data)

    def createtask_button(self):
        self.driver.find_element("xpath", "//input[@value='Create Tasks']").click()