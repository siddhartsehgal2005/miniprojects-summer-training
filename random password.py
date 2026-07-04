import random
letters = "abcdefghijklmnopqrstuvwxyz"

password = ""

for i in range(8):
    password = password + random.choice(letters)

print("Your password is:", password)