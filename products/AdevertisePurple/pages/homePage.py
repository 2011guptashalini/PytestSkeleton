from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        # locators on the page.
        self.compose_message = "//span[text()='Compose Message']"

    def click_compose_message(self):
        self.driver.find_element(By.XPATH, self.compose_message).click()

