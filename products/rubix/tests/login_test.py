import time

from selenium import webdriver
import pytest
from products.rubix.pages.loginPage import LoginPage
from products.rubix.utils import utils as utils
import allure
import moment
import unittest


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_invalidLogin(self):
        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_user_name(utils.USERNAME_INVALID)
            login.enter_password(utils.USERNAME_INVALID)
            login.click_sign_in()
            time.sleep(2)
            assert login.toaster_present() == True
        except AssertionError as error:
            print("Error message is not displayed")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/PytestSkeleton/products/rubix/screenshots/" + screenshotName + ".png")
            raise

    def test_noCredential(self):
        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            time.sleep(1)
            login.enter_no_user_name()
            login.click_sign_in()
            time.sleep(2)
            assert login.error_present() == True
        except AssertionError as error:
            print("Error message is not displayed")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/PytestSkeleton/products/rubix/screenshots/" + screenshotName + ".png")
            raise

    def test_login(self):
        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_user_name(utils.USERNAME_CORRECT)
            login.enter_password(utils.PASSWORD_CORRECT)
            login.click_sign_in()
            time.sleep(2)
            title_page = driver.title
            assert title_page == 'Rubix'
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/PytestSkeleton/products/rubix/screenshots/" + screenshotName + ".png")
            raise
