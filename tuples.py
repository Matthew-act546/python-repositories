#defining a tuple just like list but instead of square brackets we use parentheses
#tuple are immutable!
tuple = (200, 50, 30)
print(tuple)

#not gonna work 
#tuple[0] = 70

#accessing tuple
print(tuple[0])
print(tuple[1])
print(tuple[2], end="\n\n")

#looping all value of tuples
for tuples in tuple:
    print(tuples)
print()

#writing over a tuple
tuple = (2, 4, 6, 8, 10)
print("even number:", end=" ")
for tuples in tuple:
    print(tuples, end=" ")
print()

#writing over it.....
tuple = (1, 3, 5, 7, 9)
print("odd number: ", end=" ")
for tuples in tuple:
    print(tuples, end=" ")

