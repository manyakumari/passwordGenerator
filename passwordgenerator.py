import random

def passwordmaker(passlength,passnum):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#$&"

    #passlength = int(input("How many characters does the password need to be? "))
    #passnum = int(input("How many passwords do you want? "))

    possiblechtrs = len(characters)

    for i in range(passnum):
        password = []
        for i in range(passlength):
            randindex = random.randint(0,possiblechtrs)
            password.append(characters[randindex])
        actualpassword = "".join(password)
        print("Password suggestion: ", actualpassword)

passwordmaker(10,4)