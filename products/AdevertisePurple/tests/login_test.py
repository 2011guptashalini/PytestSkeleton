import time

from selenium import webdriver
import pytest
from products.AdevertisePurple.pages.loginPage import LoginPage
from products.AdevertisePurple.utils import utils as utils
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    @pytest.mark.order(1)
    def test_login(self):

        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_user_name(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            time.sleep(2)
            login.click_sign_in()
            title_purply = driver.title
            assert title_purply == 'Advertise Purple Business Intelligence'
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/PytestSkeleton/products/AdevertisePurple/screenshots/" + screenshotName + ".png")
            raise
