import re

def user_name_validator(user_name):
    if re.match(r"^[a-zA-Z\d]{10,20}$", user_name.get()):
        return user_name
    else:
        raise ValueError("Invalid username")


def password_validator(password):
    if re.match(r"^[a-zA-Z\d]{8,14}$", password.get()):
        return password
    else:
        raise ValueError("Invalid username")


def nick_name_validator(nick_name):
    if re.match(r"^[a-zA-Z\d\s$@#]{3,30}$", nick_name.get()):
        return nick_name
    else:
        raise ValueError("Invalid username")