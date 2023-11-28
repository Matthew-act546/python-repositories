def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza size with the following toppings: ")
    for topping in toppings:
        for tops in topping:
            print(f"\t- {tops.title()}")

top = []
while True:
    topps = str(input("Press Q to quit\nEnter Toppings you want in your pizza: "))
    top.append(topps)
    if topps.lower() == 'q':
        del top[-1]
        pizza_size = int(input("Enter a pizza size(inch): "))
        make_pizza(pizza_size, top)
        break
