print("\n" + "list type!")

#create list
flavor_list = ['chocolate', 'milk', 'sweat corn', 'mango']
print(flavor_list, end="\n\n")

#acessing list
print("accessing list")
print("My favourite flavor is " + flavor_list[0] + " and my hated flavor is " + flavor_list[2])

#.title() - title function
print("I hate " + flavor_list[2].title() + " because i hate corn.", end="\n\n")

#modifying list
print("modifying list")
flavor_list[0] = "double dutch"
print(flavor_list, end="\n\n")

#adding/appending to the list
print("adding/appending list")
flavor_list.append('ube')
print(flavor_list, end="\n\n")

#inserting list
print("inserting list")
flavor_list.insert(0, "cheese")
print(flavor_list, end="\n\n")

#removing/deleting forever!
print("removing list")
del flavor_list[1]
print(flavor_list, end="\n\n")

#pop() removing the last item in the list
print("pop() func")
popped_flavor = flavor_list.pop()
print(popped_flavor)
print(flavor_list, end="\n\n")

#popping items from any position of the item in list
print("popping list from any position in list")
hated_flavour = flavor_list.pop(2)
print("bye " + hated_flavour + " i hate u goodbye!")
print(flavor_list, end="\n\n")

#removing item in list..... make sense RIGHT? just look the code!
print("removing item in list ")
flavor_list.remove("cheese")
print("I remove cheese because it's too yummy!")
print(flavor_list, end="\n\n")


######################## ORGANIZING LIST! #########################
print("\n" + "~~~~~ ORGANING LIST ~~~~~")
linux_distro = ['ubuntu', 'kali', 'parrot', 'rasberry pi']
print('linux distro list =', linux_distro, end="\n\n")

#sort using sorted() function
print("sorting using sorted() function")
print(sorted(linux_distro), end="\n\n")

#sorting list
print("sort list")
linux_distro.sort()
print(linux_distro, end="\n\n")

#reverse sorting list
print("reverse sort list") 
linux_distro.sort(reverse=True)
print(linux_distro, end="\n\n")

linux_distro2 = ['ubuntu', 'kali', 'parrot', 'rasberry pi']
