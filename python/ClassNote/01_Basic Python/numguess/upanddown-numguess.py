import random


answer = random.randint(1, 100)
print(answer)

username = input("What is your name? ")

while True:
	guess = eval(input("Hi, " + username + ". Type the number: "))

	if guess == answer:
		print("Correct!")
		break
	elif guess > answer:
		print("The answer is smaller than you think")
	elif guess < answer:
		print("The answer is bigger than you think")
	else: 
		print("You are wrong!")

# 해당 질문은 메인목표가 있으므로 우선순위를 정하는 데에 의미가 없다.
