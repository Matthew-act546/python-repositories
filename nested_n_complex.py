age = 15
young_looking = False
programmer = True

# Complex Conditional
if (age < 18 or young_looking) and programmer:
	print("Welcome programmer minors yeah yow", end="\n\n")
else:
	print("Sorry this is for MINORS programmers", end="\n\n")
	
# nested if statement
if age < 18 or young_looking:
	if programmer:
		print("Welcome programmer minorss!!!")
	else:
		print("WHAT!!! you're not a programmer....XD")
else:
	print("sorry you're not allow in this party")