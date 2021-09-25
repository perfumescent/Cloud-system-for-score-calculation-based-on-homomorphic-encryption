import rsa
import pandas as pd

def generate(id: int):
    (pub, pri) = rsa.newkeys(512)
    data = pd.read_csv("user.csv")
    data.loc[data.id==id,'privateKey'] = pri
    data.to_csv("user.csv",index=False)
    with open(str(id)+".key","w") as f:
        f.write(str(pub))