import inspect

# CONSTANTS

URL = "URL OF THE PROJECT"
USERNAME = "2011guptashalini@gmail.com"
PASSWORD = "Test@2006"


def whoami():
    return inspect.stack()[1][3]
