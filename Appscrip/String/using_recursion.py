#WAP to reverse a given string using recursion.
def reverse_string(str):
    if len(str) == 0:
        return (str) 
    else:
        string1=reverse_string(str[1:])
        return (string1 + str[0])

print(reverse_string(input('enter string')))