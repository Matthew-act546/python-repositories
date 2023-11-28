response = {}

active = True

while active:
    name = input("Enter your name: ")
    want_gift = input("Enter your wish gift for birthday: ")
    
    response[name] = want_gift
    add_person = input("Do you want to add a person? Y/N ")
    if add_person.lower() == 'n':
        active = False

for name, gift in response.items():
    print(f"\n{name} want a {gift} when her Birthday comes!")