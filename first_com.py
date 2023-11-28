all_type, eac_char, eac_int, eac_float, eac_bool = [], [], [], [], []


while True:
   entered = input("Enter q to quit\nEnter some different data types: ").title()
   
   if entered == 'Q':
      print(all_type)
      break
   elif entered == "True" or entered == "False":
      all_type.append(bool(entered))
   else:
      all_type.append(entered)


for eac_all in all_type:
   if type(eac_char) == str:
      eac_char.append(eac_all)
      
   elif type(eac_int) == int:
      eac_int.append(eac_all)
   
   elif type(eac_float) == float:
      eac_float.append(eac_all)

   elif type(eac_bool) == bool:
      eac_bool.append(eac_all)