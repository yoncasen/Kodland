import random

def gen_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&'()*+,^-./:;<=>?[]_`{~}|"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def toss():
    coin = random.randint(0, 2)
    if coin == 0:
        return "YAZI"
    else:
        return "TURA"
    
# print(gen_pass(10))