capitals_dict = {
'Kerala' : 'Trivandrum',
'Tamilnadu' : 'Chennai',
'Karnataka' : 'Bangalore',
'Andrapradesh' : 'Hyderabad',
'Goa' : 'Panaji',
'Maharashtra' : 'Bombay',
'Madhyapradesh' : 'Bhopal',
'West Bengal' : 'Calcutta',
'Orissa' : 'Bhuvaneshwar',
'Bihar' : 'Patna',
}
import random

states = list(capitals_dict.keys())
print(states)
print(len(states))
print ("Do you want to quit? if so, enter quit")
while True:
	state = random.choice(states)
	capital = capitals_dict[state]
	capital_guess = input("Whats the capital of " + state + "?")
	if capital_guess == "quit":
		break
	elif capital_guess == capital:
		print("Correct! Nice job")
	else:
		print("Incorrect. The capital of " + state + " is " + capital +".")
print("All done")