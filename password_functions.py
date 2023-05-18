import random

def easy(password):
    #basic shuffle of existant characters
    char_list = list(password)
    random.shuffle(char_list)
    return "".join(char_list)

def medium(password, characters):
    #along with shuffling password, add some numbers in
    result = ""
    char_list = list(password)
    random.shuffle(char_list) and random.shuffle(characters)
    joined_list = "".join(char_list)
    for x in joined_list:
        result += str(random.choice(characters))
        result += x

    return result

def hard(password, range_of_numbers):
    #take list of numbers alternating between adding them as they are and then converting to letters 
    result = ""
    char_list = list(password)
    random.shuffle(char_list)
    joined_list = "".join(char_list)
    flag = True
    for x in joined_list:
        if flag == True:
            result += x; result += str(random.choice(range_of_numbers))
            flag = False
        elif flag == False:
            result += x; result += str(chr(random.choice(range_of_numbers)))
            flag = True


    return result