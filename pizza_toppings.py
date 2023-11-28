prompt = "\nEnter a toppings that you want to include in your pizza!\n(enter x to quit)"

toppings_add = []

while True:
    toppings = input(prompt)

    if(toppings == "x"):
        print(toppings)
        break
    else:
        print(f"{toppings} adding")
