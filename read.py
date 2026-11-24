
import os

username = os.getenv('USERNAME_ENV')
password = os.getenv('PASSWORD_ENV')

if username is None:
    print("Username environment variable is missing")
else:
    print("Username received:", repr(username))

if username and username.strip() == 'ADMIN':
    print("valid")
else:
    print("invalid")
