users = {
    'matthew': {
        'first': 'Matthew David',
        'last': 'Fernandez',
        'location': 'Metro Manila',
    },

    'gabriel': {
        'first': 'Miclawrence',
        'last': 'Fernandez',
        'location': 'Metro Manila',
    },
}

for username, value in users.items():
    print("Username: " + username.title())
    full_name = value['first']+ " " + value['last']
    location = value['location']
    
    print("\tFull Name: ", full_name.title())
    print("\tLocation: ", location.title())
    print()

#