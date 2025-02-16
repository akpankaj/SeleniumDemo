from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker
from utilites import excel_utlity_file

class Test_02_Admin_Login_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger=Log_Maker.log_gen()
    path = ".\\test_data\\admin_login_data.xlsx"
    status_list=[]

    #invalid_username = Read_Config.get_invalid_username()
    def test_valid_admin_login_data_driven(self,setup):
        self.driver=setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)

        self.rows =excel_utlity_file.get_row_count("self.path","Sheet1")
        print("No of rows",self.rows)

        for r in range(2,self.rows+1):
            self.username = excel_utlity_file.read_data("self.path","Sheet1",r,1)
            self.username = excel_utlity_file.read_data("self.path", "Sheet1", r, 2)
            self.username = excel_utlity_file.read_data("self.path", "Sheet1", r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            sleep(5)
            act_title=self.driver.title
            exp_title='Demo Web Shop'

            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")
                    self.admin_lp.logout_btn()
                elif self.exp_login =="No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Failed")
                    self.admin_lp.logout_btn()
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("Failed")
                elif self.exp_login =="No":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")

        print("Status list is",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("test admin data driven is failed")
            assert False
        else:
            self.logger.info("test admin data driven is failed")
            assert True





