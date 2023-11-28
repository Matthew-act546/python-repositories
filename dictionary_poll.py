favourite_langguage = {
   'matthew': "python",
   'sarah': "C",
   'dave': "javascript",
   'jophil': "C++",
}
friends = ['dave', 'sarah']
for keys in favourite_langguage.keys():
   print(keys.title())

   if keys in friends:
      print("  Hi " + keys.title() + " i hear you're favourite langguage is " + favourite_langguage[keys].title())
      
if 'joseph' not in favourite_langguage.keys():
   print("joseph please take our poll!")
print()

for name in sorted(favourite_langguage.keys()):
   print(name.title() + " Thank you for the answering to our poll!")
