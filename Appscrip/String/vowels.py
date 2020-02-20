# WAP to count the number of vowels and consonants in a given string.


vowels="aeiou"  #declaring the vowels in variable named as vowels

count_of_vowels=0
count_of_consonants=0

# asking for input of  string
input1=list(input("enter a string").lower())

for each_char in input1:
	if each_char not in vowels:
		count_of_consonants+=1
	else:
		count_of_vowels+=1


print("count of vowels is",count_of_vowels)            #printing count of vowels 
print("count of consonants is",count_of_consonants)    #printing count of consonants
