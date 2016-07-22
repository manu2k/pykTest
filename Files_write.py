f = open("c:\python\scores.txt","w")

while True:
	participant = input("Participant name > ")
	if participant == "quit":
		print("Quitting...")
		break
	score = input("Score for " + participant + "> ")
	f.write(participant + "," + score + "\n")
	
f.close()