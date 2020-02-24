
# WAP to find all pairs of an integer array whose sum is equal to a given number.


def sum_equal_to_given_number(list_of_nums):   
	input1=int(input("enter a num"))                                       # Giving the number 30 
	pairs_of_list=[]

	for num1 in range(len(list_of_nums)):                                  
		for num2 in range(len(list_of_nums)):
			if list_of_nums[num1]!=list_of_nums[num2]:                     #stopped to repeated numbers in list_of_numbers
				if list_of_nums[num1]+list_of_nums[num2]==input1:
					pair=[list_of_nums[num1],list_of_nums[num2]]
					if pair not in pairs_of_list:
						pairs_of_list.append(pair)
	if len(pairs_of_list)>0:
		return pairs_of_list       											#returing pairs of numbers if pairs are there
	else:
		return "There are no pairs"                                         #returning value to function if no pairs are there
print(sum_equal_to_given_number([11,20,18,25,12,19,29,10,19]))              