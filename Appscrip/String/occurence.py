# WAP to count the occurrence of a given character in a string.
input1=input("enter string")
output_dict_with_occurences={}
for each_char in input1:
    counter=0
    for check_char in input1:
        if each_char==check_char:                        #if both characters are equal it will increase the count after checking of each char from a list
            counter+=1
    output_dict_with_occurences[each_char]=counter       #if count of each character came it will create key and value pairs of those numbers
print(output_dict_with_occurences)