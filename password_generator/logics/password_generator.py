import string
import random
from flask import redirect, url_for, Blueprint, request

generate_password = Blueprint("generate_password", __name__)

@generate_password.route("/generate_password")
def generate_random_password():
    letters_list = []
    lengthValue = request.args.get("lengthValue", 0)
    given_limit = int(lengthValue) if lengthValue else 0

    lower = request.args.get("lowercaseCheck")
    upper = request.args.get("uppercaseCheck")
    number = request.args.get("numbersCheck")
    special = request.args.get("specialCheck")
    
    if lower == "on":
        letters_list.append(string.ascii_lowercase)

    if upper == "on":
        letters_list.append(string.ascii_uppercase)

    if number == "on":
        letters_list.append(string.digits)

    if special == "on":
        letters_list.append(string.punctuation)

    letters_string = "".join(letters_list)
    lower_limit = 8
    upper_limit = 32

    if given_limit < lower_limit:
        limit = lower_limit
    elif given_limit > upper_limit:
        limit = upper_limit
    else:
        limit = given_limit

    return "".join(random.choices(letters_string, k=limit)) if letters_string else ""
