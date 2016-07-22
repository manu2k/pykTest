#names = ["Alice","Bob","Amy"]
#for name in names:
#	print("Members are " + name)
#for i in [0,1,2,3,4]:
	#print("Hello" + str(i))

counter = 0
while counter <5:
		print("Hello " + str(counter))
		counter = counter + 1
print("")		
count = 0
while True:
	print("Hello " + str(count))
	count = count + 1
	if count >=5:
		break

print("Hello human!")

while True:
	user_input = input("> ")
	if user_input == "quit":
		print("Goodbye!!!")
		break
	else:
		print(user_input)