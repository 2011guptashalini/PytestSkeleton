import inspect
from products.AdevertisePurple.pages.loginPage import LoginPage
from products.AdevertisePurple.utils import utils as utils

# CONSTANTS

URL = "https://staging.purplyapp.com/sign-in"
USERNAME = "2011guptashalini@gmail.com"
PASSWORD = "Test@2006"


def whoami():
    return inspect.stack()[1][3]


