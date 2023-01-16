from selenium import webdriver
from selenium.webdriver.common.by import By


# This is a very common file and an example to start coding pages like this.
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # Locator of the elements on the page
        self.username_xpath = "//input[@id='email']"
        self.password_xpath = "//input[@id='password']"
        self.signIn_btn_xpath = "//span[text()='Login']"
        #toaster message
        self.invalid_error_xpath = "//*[text()='Invalid Credentials']"
        #error
        self.email_req_xpath = "//p[text()='Email is required']"

    def enter_user_name(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enter_no_user_name(self):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys("\n")

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.signIn_btn_xpath).click()

    def toaster_present(self):
        return self.driver.find_element(By.XPATH, self.invalid_error_xpath).is_displayed()

    def error_present(self):
        return self.driver.find_element(By.XPATH, self.email_req_xpath).is_displayed()

