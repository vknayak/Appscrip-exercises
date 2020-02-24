# WAP to find the largest and smallest number in an unsorted integer array.

# list_of_numbers=#List of numbers



def small_and_large(list_of_numbers): #defining a function named as small_and_large
	max_num=list_of_numbers[0]    #declaring first element of a list as a maximum number
	min_num=list_of_numbers[1]    #declaring second element of a list as a minimum number

	for each_num in list_of_numbers:
		if each_num>max_num:             #if our guessed maximum number is less than number coming from iteration it will swap the numbers
			max_num=each_num
		if each_num<min_num:             #if our guessed minimum number is greater than the number coming from iteration it will swap numbers
			min_num=each_num

	print("Maximum number in this list is",max_num)
	print("Minimum number in this list is",min_num)

small_and_large([-50,30,4,2,8,10,20,25,0,-100,-2]) # calling user defined function

