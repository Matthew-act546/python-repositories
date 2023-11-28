list_greet= []
while True:
    print("Welcome to our app greeter kindly...")
    first = input("Enter your first name here: ")
    last = input("Enter your last name here: ")
    full_name = f"{first} {last}"
    list_greet.append(full_name)

    print("NOTED!!!\nDo you want to continue it?(y/n)")
    response = input()
    if response == "y":
        first = input("Enter your first name here: ")
        last = input("Enter your last name here: ")
        full_name = f"{first} {last}"
        list_greet.append(full_name)
    
    else:
        print("These are the list of people that we greet")
        for greets in list_greet:
            print(f"- {greets.title()}")
        break

    
       








