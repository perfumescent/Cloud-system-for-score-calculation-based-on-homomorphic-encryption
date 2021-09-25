from flask import Flask, render_template, request, flash, url_for, redirect
import pandas as pd
import rsa

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev' 

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        status = request.form.get('status')
        data = pd.read_csv("user.csv")
        
        if len(data[data.id==int(id)])>0:
            flash("你已经申请过安全令！")
            return render_template('register.html')
        
        (pub, pri) = rsa.newkeys(512)
        data.loc[len(data)] = (id,name,status,None,pri)
        data.to_csv("user.csv",index=False)
        with open("./Keys/"+status+name+str(id)+".key","w") as f:
            f.write(str(pub))
        flash("成功向教务发送申请！请等待相关人员下发安全令文件。")
        return render_template('register.html')

    return render_template('register.html')