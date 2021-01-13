from pwn import xor

def anyScore(s):
 score = 0
 for c in s:
  if 32 <= ord(c) and ord(c) <= 126:
   score += 1
 return score

def alphaScore(s):
 score = 0
 for c in s:
  if 32 == ord(c) or (65 <= ord(c) and ord(c) <= 90) or (97 <= ord(c) and ord(c) <= 122):
   score += 1
 return score

a = bytes.fromhex(open('c3.in','r').read().strip())

ms, xx = 0, 0
for _ in range(128):
 x = xor(a,_)
 s = anyScore(x.decode())
 aas = alphaScore(x.decode())
 #print("0x{:x} {}\n{}, {}\n".format(_,x,s,aas))
 ss = min(s,aas)
 if ss > ms:
  ms = ss
  xx = _

print(xor(a,xx).decode())