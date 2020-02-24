# WAP to find all permutations of a string.WAP to find all permutations of a string.

input1=input("enter a string to know permutations of string: ")

for i in input1:
	for j in input1:
		for k in input1:
			if (i!=j) and (i!=k) and (j!=k):                   #takes the elements where they don't have duplicates
				print(i+j+k)