
p=input("Enter the password to check it's validity: ")
smallL=0
capsL=0
numb=0
spchr=0
l=len(p)
if(l>=6 and l<=12):
	for character in p:
		if character.isupper():
			capsL+=1
		elif character.islower():
			smallL+=1
		elif character.isdigit():
			numb+=1
		elif(character=="$" or character=="#" or character=="@"):
			spchr+=1
		else:
			print("Invalid Password")
			break
	if(capsL>0 and smallL>0 and numb>0 and spchr>0):
		print("The password entered is valid")
	else:
		print("The password entered is not valid")
else:
	print("The password entered exceeds the limit or does not reach the minimum character limit")
