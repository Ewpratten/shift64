import secrets
import string

def ModKey(key:str, message:str):
	key = float(key)
	if ord(message[0]) % 2 == 0:
		key *= len(message)
	else:
		key += len(message)
	return str(key).split(".")[0]

def UnModKey(key:str,message:str):
	key = float(key)
	if ord(message[0]) % 2 == 0:
		key /= len(message)
	else:
		key -= len(message)
	return str(key).split(".")[0]

def GenKey(message:str):
	return str(secrets.randbelow(len(message)*10000015))

def GenCycleKey():
	output = "0"
	for _ in range(1, secrets.randbelow(10)):
		output += secrets.choice(["0","1","2","3"])
	output += "@"
	output += str(secrets.randbelow(10)+ 2)
	return output

def Entropy(message):
	return message + secrets.choice(string.ascii_lowercase)

def UnEntropy(message):
	return message[:-1]