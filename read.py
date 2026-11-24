import os
username = os.getenv('USERNAME_ENV')
password = os.getenv('PASSWORD_ENV')

if username=='admin':
    print("valid")
else:
    print("invalid")
    