

#WAP to find the missing number in a given integer array of 1 to 100.

def find_missing_num(user_given_list):
	list_of_nums=list(for num in range(1,101))            #list of all numbers from 1 to 100
	for each_num in list_of_nums:
		if each_num not in user_given_list:               #it will check each number from list of all numbers is there or not in user given list
			print(each_num)


find_missing_num()                                #give a list here as a parameter