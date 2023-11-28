prompt = "How many you will register?"

register = int(input(prompt))
total = []
i = 1
while i <= register:
    age_register= int(input(f"How old the {i}: "))
    if(age_register < 3):
        print(f"This person ticket is free")
    elif(age_register <= 11 and age_register >=3):
        charge = 10
        print(f"This person ticket is charge by {charge} dollars")
        total.append(charge)
    else:
        charge = 15
        print(f"This persons ticket is charge by {charge} dollars")
        total.append(charge)
    i += 1

for i in range(int(len(total))):
    i += total[i]
    print(i)