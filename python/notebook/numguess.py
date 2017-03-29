import random



answer = random.randint(1, 100)
print(answer)


username = input("what is your name? ")
print(username)

guess = eval(input("Hi, " + username + ". guess the number: "))  
print(guess)

if guess == answer:
	print("Correct!")
else:
	print("Wrong!")

