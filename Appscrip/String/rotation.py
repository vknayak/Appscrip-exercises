# WAP to check if two strings are a rotation of each other.



def check_rotation(str1,str2):
	if len(str1)==len(str2):                                    #the length has to equal otherwise they are not in rotation
		str1=str1+str1
		if str2 in str1:                                                        
			print("They are rotation of each other")            #after adding string if string2 in str1 they are rotation of each other
		else:
			print("They are not a rotation of each other")

	else:
		print("They are not a rotation of each other")

string1=input("Enter string1:")
string2=input("Enter string2:")
check_rotation(string1,string2)