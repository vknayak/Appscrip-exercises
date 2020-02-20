
# WAP to find duplicate numbers in an array if it contains multiple duplicates.

def duplicate_numbers(user_given_list):
	numbers_list=[]
	multiple_duplicates=[]
	for i in user_given_list:                                 
		if i not in numbers_list:
			numbers_list.append(i)                             #we will get a list of numbers from a given list without any duplicate
	for each_char in numbers_list:
		count_of_each_char=0
		for check_char in user_given_list:
			if each_char==check_char:
				count_of_each_char+=1                                       #we are calculating the how many times it is coming
		if count_of_each_char>1:                                            #if the count is greater than 1 means it came more than 2 times so we are printing tha number
			multiple_duplicates.append(each_char)
	if len(multiple_duplicates)>1:
		print(multiple_duplicates)
	else:
		print(f"There is only duplicate integer is there that is ",multiple_duplicates[0])

duplicate_numbers([10,20,30,40,10])                        #enter a list as a parameter for example [10,20,30,40,10,20] 

#if [10,20,30,40,10,20] this list contains multiple duplicates like 10,20 use this list then it will list of two numbers
