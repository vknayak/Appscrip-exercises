
# WAP to check if two strings are anagrams of each other.
def anagram_finder(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    if list_str1 == list_str2:
        return('They are Anagrams!')
    else:
        return('They are not Anagrams!!')


user1=input('Enter the first input: ')
user2=input('Enter the second input: ')
print(anagram_finder(user1,user2))