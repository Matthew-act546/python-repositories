print("What is your favorite games give us 3") 

#list of the game
fav_game = ['', '', '']

#input for favorite games
fav_game[0] = input("1st Game:")

fav_game[1] = input("2nd Game:")

fav_game[2] = input("3rd Game:")

line = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

if fav_game[0] == "" or fav_game[1] == "" or fav_game[2] == "":
	print("\n\nERROR!" + line + "You didn't enter a value in 1st,2nd\nor 3rd game do the question again" + line)
else:
	print("\nYou're favourite game is\n" + str(fav_game))

	print("\nDo you want to replace your favourite game? yes or no")
	replace = input()
	if replace.lower() == "yes":
		print("What games do you want to replace?")
		want_rep = input()
		if want_rep == fav_game[0]:
			print("What name do you want to replace")
			del fav_game[0]
			inserting = input()
			fav_game.insert(0, inserting)
			print("\n\nFINAL REPORT!"+ line + "This is you're favorite game\n" + str(fav_game) + "\nThank you!!! for answering the\nquestion have a nice day!\n" + line)
		elif want_rep == fav_game[1]:
			print("What name do you want to replace")
			del fav_game[1]
			inserting2 = input()
			fav_game.insert(1, inserting2)
			print("\n\nFINAL REPORT!"+ line + "This is you're favorite game\n" + str(fav_game) + "\nThank you!!! for answering the\nquestion have a nice day!\n" + line)
		elif want_rep == fav_game[2]:
			print("What name do you want to replace")
			del fav_game[2]
			inserting3 = input()
			fav_game.insert(2, inserting3)
			print("\n\nFINAL REPORT!"+ line + "This is you're favorite game\n" + str(fav_game) + "\nThank you!!! for answering the\nquestion have a nice day!\n" + line)
		elif want_rep == "" or want_rep == " ":
			print("ERROR"+ line + "You don't enter a game..." + line)
		else:
			print("\nERROR" + line + "Input the correct letter. Pls try\nagain.." + line)
	elif replace.lower() == "no":
		print(line, end="")
		print("Very Good you already manage you're\nfavourite game and that is\n" + str(fav_game) + "\nThank you for answering this questionhave a nice day!" + line)
		
	else:
		print("ERROR" + line + "Did you say yes or no?" + line)
