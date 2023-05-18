import random
import password_functions as pf
print("Welcome to the password generator!")
print("What level difficulty would you like to choose?")
level = input("Choose easy, medium, or hard\n")
level_diffifulty = level.lower()
characters = range(1, 11)
range_of_numbers = range(32, 127)

if level_diffifulty == "easy" or level_diffifulty == "medium" or level_diffifulty == "hard":
    any_case_password = input("What is your initial password?\n")
    initial_password = any_case_password.lower()
    if level_diffifulty == "easy":
        print(pf.easy(initial_password))

    elif level_diffifulty == "medium":
        print(pf.medium(initial_password, characters))

    elif level_diffifulty == "hard":
        print(pf.hard(initial_password, range_of_numbers))
        
else:
    print("Try again")
