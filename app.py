from flask import Flask, render_template, request, flash, url_for, redirect, session
import pandas as pd
import rsa

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev' 

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = int(request.form.get('id'))
        data = pd.read_csv("user.csv")

        if len(data.loc[data.id==id])==0:
            flash("用户不存在，请先申请安全令！")
            return render_template('register.html')

        session['id']=id

        if pd.isnull(data.loc[data.id==id].identity[0]):
            return redirect(url_for('set'))
        
        return redirect(url_for('authentication'))
        
    return render_template('index.html')

@app.route('/set', methods=['GET', 'POST'])
def set():
    if request.method == 'POST':
        psw = request.form.get('psw')
        data = pd.read_csv("user.csv")
        data.loc[data.id==int(session['id']),'identity']=psw
        data.to_csv("user.csv",index=False)
        return redirect(url_for('authentication'))
        
    return render_template('set.html')

@app.route('/authentication', methods=['GET', 'POST'])
def authentication():
    if request.method == 'POST':
        psw = request.form.get('psw')
        data = pd.read_csv("user.csv")
        if data[data.id==int(session['id'])].identity[0]==psw:
            return(redirect(url_for('download')))
        flash("鉴别码错误！")
    return render_template('authentication.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = int(request.form.get('id'))
        name = request.form.get('name')
        status = request.form.get('status')
        data = pd.read_csv("user.csv")
        
        if len(data.loc[data.id==id])>0:
            flash("你已经申请过安全令，请勿重复！")
            return render_template('register.html')
        
        (pub, pri) = rsa.newkeys(512)
        pub = pub.save_pkcs1()
        pri = pri.save_pkcs1()
        data.loc[len(data)] = (id,name,status,None,pri)
        data.to_csv("user.csv",index=False)
        with open("./Keys/"+status+name+str(id)+".pem","wb") as f:
            f.write(pub)
        flash("成功向教务发送申请！请等待相关人员下发安全令文件。")
        return render_template('register.html')

    return render_template('register.html')