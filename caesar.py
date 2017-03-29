import string
from string import ascii_uppercase as up_case
from string import ascii_lowercase as lo_case


# caesar 함수 시작(s = msg, k = encrypt_key, decode(True or False)
def caesar(s, k, decode = False):
	if decode:
		k = 26 - k


	return s.translate(
		str.maketrans(
			up_case + lo_case,
			up_case[k:] + up_case[:k] +
			lo_case[k:] + lo_case[:k]
			)
		)


while True:
	encrypt_key = int(input("Decide the magic number: "))
	msg = input("enter the message: ")
	print("encrypted message: ", caesar(msg, encrypt_key))
	print("decrypted message: ", caesar(caesar(msg, encrypt_key), encrypt_key, True))
	exit = input("press 'q' to quit: ")
	if exit == 'q' or exit == 'Q':
		break
