import rsa

psw = input("Please input your password:\n")
pk = input("Please input your key file name:\n")

with open(pk, mode='rb') as file:
    keydata = file.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

print(keydata)
print(pubkey)
res=rsa.encrypt(psw.encode(), pubkey)
print(res)