
answer = random.randint(1,100)
print(answer)

while input:
	guess = eval(input("Hi, " + username + ". Guess the number:"))

	if guess == answer:
		print("CORRECT!")
		break
	elif guess > answer:
		chance -= 1
		print("Too High.((%d times left)" %(chance))
	elif guess < answer:
		changce -= 1 
		print("Too Low.(((%d times left)" %(chance))

	if chance == 0:
		print("you are dead")

