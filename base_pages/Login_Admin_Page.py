from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Login_Admin_Page:
    textbox_username_id="Email"
    textbox_password_id="Password"
    btn_login_xpath="//*[@class='button-1 login-button']"
    logout_btn="Log out"
    #link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_btn).click()


    # def wait_for_homepage(self):
    #     wait = WebDriverWait(self.driver, 30)
    #     condition = visibility_of_element_located(self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1"))
    #     wait.until(condition)