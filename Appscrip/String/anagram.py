
# WAP to check if two strings are anagrams of each other.
def anagram_finder(str1, str2):
    list_of_str1 = list(str1)
    list_of_str1.sort()                                                 #we are going to sort two strings 
    list_of_str2 = list(str2)
    list_of_str2.sort()

    if list_str1 == list_str2:
        return('They are Anagrams!')
    else:
        return('They are not Anagrams!!')


string1=(input('Enter the first input: ')).lower()
string2=(input('Enter the second input: ')).lower()
print(anagram_finder(string1,string2))                      #for example dormitrory and dirtyroom