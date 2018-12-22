from coding import *
from mods import *
import sys

print(Decode(Encode(Encode("Hello","1234"),"1234"),"1234"))

if len(sys.argv) < 2:
	print("Usage: shift64 [0/1] <message>")
else:
	mode = sys.argv[1]
	inpmod = False
	if int(mode) == 0:
		inpmod = True
	else:
		print("Enter the key:")
		key = input(">")
		print("Enter the sequence key:")
		ckey = input(">")
code = str(sys.argv[2])


if inpmod:
	
	ckey = GenCycleKey()
	cycles = int(ckey.split("@")[1])
	key = GenKey(code)
	
	output = code
	
	for i in range(1,cycles):
		j = 0
		for op in ckey.split("@")[0]:
			print(f"{j} / {i} / {cycles}", end="\r")
			if int(op) == 0:
				output = Encode(output, key)
			if int(op) == 1:
				key = ModKey(key,output)
			if int(op) == 2:
				output = Entropy(output)
			if int(op) == 3:
				key, output = Swap(key,output)
			
			j += 1
	
	print(f"Key:               \n{key}\nSequence Key:\n{ckey}\n\nMessage:\n{output}")
	exit()

# decode
cycles = int(ckey.split("@")[1])
output = code
ck = []
for char in ckey.split("@")[0]:
	ck.append(char)
ckey = ck
ckey.reverse()
for i in range(1,cycles):
	j = 0
	for op in ckey:
		print(f"{j} / {i} / {cycles}", end="\r")
		if int(op) == 0:
			output = Decode(output, key)
		if int(op) == 1:
			key = UnModKey(key,output)
		if int(op) == 2:
			output = UnEntropy(output)
		if int(op) == 3:
			key, output = Swap(key,output)
		
		j += 1

print(output)