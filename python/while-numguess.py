import random


answer = random.randint(1, 100)
print(answer)

username = input("What is your name? ")

while True:
	guess = eval(input("Hi, " + username + " Type the number: "))
	
	if guess == answer: 
		print("Correct!")
		break
	else: 
		print("Wrong!")


