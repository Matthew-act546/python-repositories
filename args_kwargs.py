nums = [1, 4, 5, 76, 2, 3, 2]

print(nums)
print(*nums)

def ordered_pizza(size, *toppings, **details):
    print(f"Order size of {size} pizza")
    for topping in toppings:
        print(f"- {topping}")
    for k, v in details.items():
        print(f"{k.title()}: {v}")
ordered_pizza("Large", "macaroni", "macaroni salad", "peperoni", delivery=True, cash=True)