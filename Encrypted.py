import rsa


publicKey, privateKey = rsa.newkeys(512)

print("Enter a message for mom:")
message = input()

encMessage = rsa.encrypt(message.encode(),  

publicKey) 

is_mom = input("are you my mom?(y/n)\n")

if is_mom == 'N' or is_mom == 'n':
	print("\n---> encrypted string <---\n" + str(encMessage) + "\n") 
elif is_mom == "Y" or is_mom == "y":
	print("Decrypting Message...", end="\n")
	print(str(encMessage))
	decMessage = rsa.decrypt(encMessage, privateKey).decode()
	print("\n~~~~~~~~~~~Decrypted message~~~~~~~~~")
	print("message from mom: ", decMessage)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
	print("error")