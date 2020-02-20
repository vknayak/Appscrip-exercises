# WAP to check if a given string is a palindrome.

input1=(input("Enter a string")).lower()                  #taking input from user and converted in to small letters
reverse_string=""                                         #empty string

# by indexing we are addingg each cahracter in empty string named as reverse string

for last_char_index in range((len(input1)-1),-1,-1):
	reverse_string+=input1[last_char_index]

# checking whether reversed string and input given by user is same or not
if reverse_string==input1:
	print(f"The given string {input1} is a polindrome")
else:
	print(f"The given string {input1} is not a polindrome")

