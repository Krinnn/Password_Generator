import random
import string

def generate_password(length):
    # define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a random password of specified length
    password = ''.join(random.choice(characters) for i in range(length))

    return password

password = generate_password(12)
print(password)