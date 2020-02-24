#WAP to reverse a given string using recursion.
def reverse_string(str):
    if len(str) == 0:
        return (str)                                   #base case if length of string is 0 it will start returning string
    else:
        string1=reverse_string(str[1:])
        return (string1 + str[0])                      #recursive case to get our answer

print(reverse_string(input('enter string')))