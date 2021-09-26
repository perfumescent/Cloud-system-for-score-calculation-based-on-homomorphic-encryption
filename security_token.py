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
print("\n------你的鉴别码如下，请复制粘贴至云端验证------")
print(base64.b64encode(res).decode())
print(base64.b64encode(res).decode())
print(base64.b64decode(base64.b64encode(res).decode().encode()))
print(base64.b64decode(base64.b64encode(res).decode().encode()))
