from selenium import webdriver
from selenium.webdriver.common.by import By


# This is a very common file and an example to start coding pages like this.
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # Locator of the elements on the page
        self.username_xpath = "//input[@name='email']"  # Change it with your username xpath
        self.password_xpath = "//input[@name='password']"
        self.signIn_btn_xpath = "//*[@type='submit']"

    def enter_user_name(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.signIn_btn_xpath).submit()
        self.driver.find_element(By.XPATH, self.signIn_btn_xpath).submit()
