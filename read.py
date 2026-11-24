import os

username = os.getenv('USERNAME_ENV')

if username is None:
    print("Secret is not available")
elif username == '':
    print("Secret is available but empty")
else:
    print("Username received successfully")