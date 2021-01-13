from pwn import xor
import codecs

a,b = eval(open('c2.in','r').read())

print(codecs.encode(xor(bytes.fromhex(a),bytes.fromhex(b)),'hex').decode())
