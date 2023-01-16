from selenium import webdriver
import pytest
from products.AdevertisePurple.pages.loginPage import LoginPage
from products.AdevertisePurple.utils import utils as utils
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):

        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_user_name(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            login.click_sign_in()
            title_page = driver.title
            assert title_page == 'My Clients'
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/PytestSkeleton/products/skeleton_projects/screenshots/" + screenshotName + ".png")
            raise

