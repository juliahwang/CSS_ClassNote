import random



answer = random.randint(1, 100)
print(answer)

username = eval(input("what is your name? "))
print(username)

guess = eval(input("Hi, " + username + ". Guess the number: "))  
print(guess)

if guess == answer:
	print("Correct!")
else:
	print("Wrong!")

