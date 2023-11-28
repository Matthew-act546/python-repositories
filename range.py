#Creating a list using list and range function
numbers = list(range(1, 6))
print(numbers, end="\n\n")

#Creating step using range functiom
even_numbers = list(range(0, 11, 2))
odd_number = list(range(1, 11, 2))
print("This is odd numbers! " + str(odd_number) + "\nThis is even number" + str(even_numbers), end="\n\n")

#Simple statistics using list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min_num = min(numbers)
max_num = max(numbers)
sum_num = sum(numbers)
print("Original numbers on the list", numbers)
print("The minimum number on the list is ", min_num)
print("The maximum number on the list is ", max_num)
print("The sum of all numbers is ", sum_num) #1+2+3+4+5+6+7+8+9+0 = 45

#LIST COMPREHENSION
squared = [value**2 for value in range(1, 11)]
print(squared)
