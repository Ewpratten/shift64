from base64 import b64decode
from base64 import b64encode

def encode(data, key):
  output = []
  data_len = len(data)
  for i in range(0, len(data) - 1):
    output.append(chr(ord(data[i]) + int(i % data_len)
  output = ''.join(output)
  return b64encode(output.encode())

def decode(data, key):
  output = []
  
