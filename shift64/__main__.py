from base64 import b64decode
from base64 import b64encode
import string

key = "5024"
message = "Water Game 2019!"

output = []
key_len = len(key)

for i in range(0, len(message) - 1):
	# print(ord(message[i]) + int(key[i % key_len]))
	output.append(chr(ord(message[i]) + int(key[i % key_len])))

# print(output)

code = ""
for num in output:
	code += str(num)

code = b64encode(code.encode())
print(code)


# Test code
code = "XGF2aXcgSWVyZSI2NTE7=="
key = "5024"

output = []
message = b64decode(code)

key_len = len(key)
for i in range(0, len(message)):
	output.append(chr(message[i] - int(key[i % key_len])))

output = ''.join(output)
print(output)