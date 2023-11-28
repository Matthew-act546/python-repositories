def data(first, last, location, age=None, ipAddr=None):
    """A data collector and store in dictionary"""
    person = {"First Name": first, "Last Name ": last, "Location": location}
    if age and ipAddr:
        person['age'] = age
        person['ipAddr'] = ipAddr
    elif age:
        person['age'] = age
    elif ipAddr:
        person['ipAddr'] = ipAddr
    
    return person

while True:
    first_name = input("\nEnter your first name: ")
    last_name = input("Enter your last name: ")
    location = input("Enter a location: ")
    age = input("Enter Age: ")
    ipAddr = input("Enter the ip address: ")
    
    if first_name == 'q':
        break
    print(data(first_name, last_name, location, age, ipAddr))
