
answer = random.randint(1,100)
print(answer)

username = eval(input("what is your name? "))

while print:
	guess = eval(print("Hi, " + username + ". Guess the number:"))


	if guess == answer:
		print("Correct!")
		break
	elif guess > answer:
		print("too high!")
	elif guess < answer:
		print("too low!")
	else:
		print("Correct")
