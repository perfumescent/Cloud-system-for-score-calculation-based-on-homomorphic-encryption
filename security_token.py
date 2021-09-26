import rsa
import hashlib
import base64
m = hashlib.md5()
psw = input("Please input your password:\n")
pk = input("Please input your key file name:\n")

with open(pk, mode='rb') as file:
    keydata = file.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)
m.update(psw.encode())
res=rsa.encrypt(m.digest(), pubkey)
print("/n",base64.b64encode(res).decode())