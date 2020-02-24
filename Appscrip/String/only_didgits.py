#WAP to check if a string contains only digits.
def onlydigits(input_of_user):
    digits='0123456789'
    for each_char in input_of_user: 
        if each_char in digits:                 #check each character is in digits named variable or not
            pass
        else:
            return False
    return True                                # it will return True when all the characters are digits only

print(onlydigits(input("enter something to check onlydigits or not: ")))  # if you are giving total integers it will give result as true otherwise false