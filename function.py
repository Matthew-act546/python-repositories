def add():
    num1 = int(input())
    print("+")
    num2 = int(input())
    result = str(num1) + " + " + str(num2) + " = " + str((num1 + num2))
    print(result)
    if (type(num1) or type(num2)) == str:
        print("sorry string are not available here!")

add()

