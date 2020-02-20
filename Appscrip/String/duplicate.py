
# WAP to print duplicate characters in a string.

input1=input("enter a string").lower()                     #taking input from a string
strings_list=[]
for i in input1:                                 
	if i not in strings_list:
		strings_list.append(i)                             #we will get a list of characters from a given string without any duplicate
for each_char in strings_list:
	count_of_each_char=0
	for check_char in input1:
		if each_char==check_char:
			count_of_each_char+=1                                       #we are calculating the how many times it is coming
	if count_of_each_char>1:                                            #if the count is greater than 1 means it came more than 2 times so we are printing tha character
		print(each_char)

