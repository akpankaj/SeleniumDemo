from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker
class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger=Log_Maker.log_gen()
    invalid_username="pankaj12@gmail.com"

    #invalid_username = Read_Config.get_invalid_username()

    def test_title_verification(self,setup):
        self.logger.info("**************************Test_01_Admin_login********************************")
        self.logger.info("*************************Verfication_of_Admin_Page_Title********************************")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Demo Web Shop. Login":
            self.logger.info("**************************Test_title_verfication_matched********************************")

            assert True

        else:
            self.logger.info("**************************Test_verfication  not matched********************************")
            #self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            assert False


    def test_valid_admin_login(self,setup):
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text=self.driver.title
        if act_dashboard_text == "Demo Web Shop":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")

            assert False
        self.driver.close()


    # def test_invalid_admin_login(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp=Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.invalid_username)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     error_msg_text=self.driver.find_element(By.XPATH,"//li[text()='No customer account found']").text
    #     if error_msg_text == 'No customer account found':
    #         assert True
    #     else:
    #         assert False
    #         #self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
    #     self.driver.close()

