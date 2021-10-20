from phe import paillier
import json
import pandas as pd

k = input(">>> Please input your key file name:\n")
ts = input(">>> Please input your transcript file name:\n")

with open(k, "r") as f:
    js = json.load(f)
pub_rec = paillier.PaillierPublicKey(int(js["pub"]))
pri_rec = paillier.PaillierPrivateKey(pub_rec, int(js['p']), int(js['q']))

data = pd.read_csv(ts)


def h(x):
    js = json.loads(x)
    cipher = paillier.EncryptedNumber(
        pub_rec, int(js['text']), int(js['exponent']))
    return pri_rec.decrypt(cipher)


data['mark'] = data['mark'].map(h)
print(data)

flag = input("是否保存至本地？（y/n）")
if flag == 'y':
    data.to_csv('_'+k, index=False)
else:
    pass
