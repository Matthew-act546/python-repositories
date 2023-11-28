#Input Method

#Method 1 inside of input
fav_game = input("What is your favorite game?")
print(fav_game)

#Method 2 outside of input
print("and another one game")
fav_games = input()
print(str("your favorite game is ") + fav_game.upper() + " "+ fav_games.upper())