################### SLICING LIST ####################


ML_players = ['chaknu', 'wrecker', 'dogie', 'Ohmyvenus', 'bennyqt']
print(ML_players[:3])
print(ML_players[1:3])
print(ML_players[2:], end="\n\n")

################### COPYING LIST #################### 
my_foods = ['spaghetti', 'hotdog', 'pancit canton', 'itlog', 'fried chicken']
friends_foods = my_foods[:]
my_foods.append('san marino')
friends_foods.append('french fries')
print("My favourite foods is ", my_foods)
print("My friends food is ", friends_foods, end="\n\n")


################## NOT GOING TO WORK #################
not_my_foods = my_foods
print(not_my_foods)