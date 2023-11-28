fav_food = ["spaghetti", "hamburger", "french fries", "hotdog", "pancit canton", "egg"]

print("INCLUSIVE")
print("My favorite food is")
for i in range(len(fav_food)):
	print(i + 1, fav_food[i])
print()

print("\n\nEXCLUSIVE")
print("My favorite food is")
for i in range(len(fav_food)):
	
	print(i, fav_food[i])
	
print()