def greet_user(users):
    for user in users:
        print(f"Hi {user.title()} Have a good day!")

user = ["Matthew", "Sarah", "Dave"]

greet_user(user)