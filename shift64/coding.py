from base64 import b64decode
from base64 import b64encode
import string

def Encode(message:str, key:str):
	output = []
	key_len = len(key)
	
	for i in range(0, len(message) ):
		output.append(chr(ord(message[i]) + int(key[i % key_len])))
	
	code = ""
	for num in output:
		code += str(num)
		
	return b64encode(code.encode()).decode()

def Decode(message:str, key:str):
	output = []
	message = b64decode(message).decode()
	
	key_len = len(key)
	for i in range(0, len(message)):
		output.append(chr(ord(message[i]) - int(key[i % key_len])))
	
	return ''.join(output)

def Swap(x,y):
	# return (y,x)
	return (x,y)