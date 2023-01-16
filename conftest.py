import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        driver = webdriver.Firefox(GeckoDriverManager().install())

    driver.maximize_window()
    driver.implicitly_wait(50)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")
