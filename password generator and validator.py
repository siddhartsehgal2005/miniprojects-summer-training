import random
import string

class Error(Exception):
    pass

def generate():
    chars = string.ascii_letters + string.digits
    password = ""
    for i in range(8):
        password = password + random.choice(chars)
    return password

def check(pwd):
    if len(pwd) < 6:
        raise Error("Too short")
    if pwd.isalpha():
        raise Error("Add numbers")
    if pwd.isdigit():
        raise Error("Add letters")
    return "OK"

print("Generated Password:", generate())

try:
    pwd = input("Enter password: ")
    print(check(pwd))
except Error as e:
    print("Error:", e)