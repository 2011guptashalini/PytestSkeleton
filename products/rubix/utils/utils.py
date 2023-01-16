import inspect

# CONSTANTS

URL = "https://exchange.rubix.io/auth"
USERNAME_INVALID = "2011guptashalini@gmail.com"
PASSWORD_INVALID = "Test@2006"

USERNAME_CORRECT = "sapna+360@rubix.io"
PASSWORD_CORRECT = "Test@2006"

def whoami():
    return inspect.stack()[1][3]
