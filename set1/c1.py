import base64

b = open('c1.in','r').read().strip()
r = base64.b64encode(bytes.fromhex(b)).decode()

print(r)


import codecs
r = codecs.encode(bytes.fromhex(b),'base64').decode()

print(r)
