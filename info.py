def build_profile(
        first, 
        last, 
        **info):

    info["First name"] = first
    info["Last name"] = last

    return info



def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza size with the following toppings: ")
    for topping in toppings:
        print(f"\t- {topping.title()}")

