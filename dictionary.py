#a simple declaring a dictionary
matthew = {'pogi': True, 'age': 15}

#accesing in dictionary
print(matthew['pogi'])
print(matthew['age'])

#adding a key-value to the dictionary
matthew['color'] = 'brown'
matthew['relationship'] = 'single'
print("this is me", matthew)

#starting with an empty dictionary
gab = {}
gab['skin color'] = 'white/brown'
gab['like'] = 'animals'
print('this is gabgab!', gab)

#modifying values in dictionary
print(gab['like'])
gab['like'] = 'playing shooting games'
print(gab['like'])

#now we're going to play walking!
david = {'steps': 100, 'running': True}
destination = 1000
if david['running']:
   print("10 step to reach your destination while you were running")
elif not david['running'] :
   david['steps'] = 50
   print("20 steps to make it to your destination")
#nevermind my mind just blown up

#deleting a value from the dictionary
del gab['skin color']
print(gab)

#a dictionary is similar to object
favourite_bread = {
   'gabriel': "spanish bread",
   'ishin': "pande gatas",
   'matthew': "pande coco",
   'mildred': "crinkles", #is my spelling right? idc..... joke hahaha
   'bianca': "cookies"
}
#loooping key value from the dictionary
for name, value in favourite_bread.items():
   print("\nName: " + name.title()) 
   print("Favourite bread: " + value.title())
print()

#looping through keys() method
print("My siblings")
for name in favourite_bread.keys():
   print(name.title())
print()

#looping through value() method
for fav_bread in favourite_bread.values():
   print(fav_bread.title())
print()
