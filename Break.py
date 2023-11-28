langguages = ["C", "C++", "Python", "Javascript", "Java", "Ruby"]

print("What is your favorite coding language")
execute = input()

for langg in langguages:
	if langg == execute:
		print("Good choice -> " + execute)
		break
	
	print(langg + " <- not this")

