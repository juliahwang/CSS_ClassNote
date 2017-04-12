import random


answer = random.randint(1, 100)
print(answer)

username = input("What's your name? ")
chances = 3

while True:
	guess = eval(input("Hi, " + username + ". Type the number: "))

	if guess == answer:
		print("Correct!")
		break
	elif guess > answer:
		chances -= 1
		print("Too big! %d times left" % (chances))
	elif guess < answer:
		chances -= 1
		print("Too small! %d times left" % (chances))

	if chances == 0:
		print("YOU FAILED")
		break
