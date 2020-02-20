#WAP to reverse words in a given sentence without using any library method.

input='This is kumar'
list_of_words=input.split()
reversed_sentence=''
for each_word in list_of_words:
    string=''                                              #after every word string will be empty again
    for k in range(len(each_word)-1,-1,-1):
        string+=each_word[k]
    reversed_sentence+=string+" "                          #after reversing every word it will add to reversed sentence string and after the word space also
print(reversed_sentence)             