from selenium import webdriver
import pytest
from products.AdevertisePurple.pages.homePage import HomePage
from products.AdevertisePurple.pages.loginPage import LoginPage
from products.AdevertisePurple.utils import utils as utils
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestHomePage():
    @pytest.mark.order(2)
    def test_homepage(self):

        try:
            driver = self.driver
            driver.get(utils.URL)
            signIn = LoginPage(driver)
            signIn.enter_user_name(utils.USERNAME)
            signIn.enter_password(utils.PASSWORD)
            signIn.click_sign_in()
            homepage = HomePage(driver)
            homepage.click_compose_message()
            title_purply = driver.title
            assert title_purply == 'Client Communication Tool'
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
