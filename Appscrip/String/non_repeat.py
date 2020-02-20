
# WAP to print the first non-repeated character in a string.

input1=input("enter a string")                       #taking input from a string
dup_list=[]
for each_char in input1:                            
	count_of_each_char=0
	for check_char in input1:
		if each_char==check_char:
			count_of_each_char+=1                                 #we are calculating the how many times it is coming
	if count_of_each_char==1:                                     #if its count is 1 means it came only 1 time print it and break it
		print(each_char)
		break

