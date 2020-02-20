
# WAP to find the duplicate number on a given integer array.

def duplicate_numbers(user_given_list):
	numbers_list=[]
	for i in user_given_list:                                 
		if i not in numbers_list:
			numbers_list.append(i)                             #we will get a list of numbers from a given list without any duplicate
	for each_char in numbers_list:
		count_of_each_char=0
		for check_char in user_given_list:
			if each_char==check_char:
				count_of_each_char+=1                                       #we are calculating the how many times it is coming
		if count_of_each_char>1:                                            #if the count is greater than 1 means it came more than 2 times so we are printing tha number
			print(each_char)

duplicate_numbers([10,20,30,40,10,20])                        #enter a list as a parameter for example [10,20,30,40,10,20] 
