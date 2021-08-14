# takes an input, welcomes the correct user, tells everyone else to get out

name = input('What is your name? ').lower()
if name == str("dylan") :
    print("Welcome", name + "!")
else :
    print("Get out", name + "!")

