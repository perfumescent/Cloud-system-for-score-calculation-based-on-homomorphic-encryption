from flask import Flask, render_template, request, flash, url_for, redirect, session
from werkzeug.utils import secure_filename
import pandas as pd
import rsa
import base64
from phe import paillier
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
public_phe, private_phe = paillier.generate_paillier_keypair()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = int(request.form.get('id'))
        data = pd.read_csv("user.csv")

        if len(data.loc[data.id == id]) == 0:
            flash("用户不存在，请先申请安全令！")
            return render_template('register.html')

        session['id'] = id
        if (data.loc[data.id == id].identity == "Null").any():
            return redirect(url_for('set'))

        return redirect(url_for('authentication'))

    return render_template('index.html')


@app.route('/set', methods=['GET', 'POST'])
def set():
    if request.method == 'POST':
        idtt = base64.b64decode(request.form.get('psw').encode())
        data = pd.read_csv("user.csv")

        pri_str = base64.b64decode(data.loc[data.id == int(
            session['id']), 'privateKey'].values[0].encode())
        pri = rsa.PrivateKey.load_pkcs1(pri_str)
        content = base64.b64encode(rsa.decrypt(idtt, pri)).decode()

        data.loc[data.id == int(session['id']), 'identity'] = content
        data.to_csv("user.csv", index=False)
        flash("设置成功，请登录！")
        return redirect(url_for('authentication'))

    return render_template('set.html')


@app.route('/authentication', methods=['GET', 'POST'])
def authentication():
    if request.method == 'POST':
        try:
            idtt = base64.b64decode(request.form.get('psw').encode())
            data = pd.read_csv("user.csv")

            pri_str = base64.b64decode(data.loc[data.id == int(
                session['id']), 'privateKey'].values[0].encode())
            pri = rsa.PrivateKey.load_pkcs1(pri_str)

            content = base64.b64encode(rsa.decrypt(idtt, pri)).decode()
            if (data[data.id == int(session['id'])]
                    .identity == content).any():
                if (data[data.id == int(session['id'])]
                        .status == "教师").any():
                    return (redirect(url_for('upload')))
                else:
                    return(redirect(url_for('download')))
        except Exception as e:
            print("------", session['id'], "------", e)
        flash("鉴别码错误！")

    return render_template('authentication.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        course = request.form.get('course')
        credit = request.form.get('credit')
        
        f = request.files['file']
        place = "transcripts/"+secure_filename(f.filename)
        f.save(place)

        mark = pd.read_csv('mark.csv')
        if (mark.course == course).any():
            flash("该科成绩已有记录，请勿重复上传！")
            return render_template('upload.html')
        data = pd.read_csv(place).iloc[:, 1:]

        data['course'] = [course for i in range(len(data))]
        data['credit'] = [credit for i in range(len(data))]
        data['mark'] = data['mark'].map(
            lambda x: str(public_phe.encrypt(int(x)).ciphertext()))

        res = pd.concat([mark, data])
        res.to_csv("mark.csv", index=False)
        flash(course+" 成绩上传成功！")

    return render_template('upload.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        status = request.form.get('status')
        data = pd.read_csv("user.csv")

        if len(data.loc[data.id == id]) > 0:
            flash("你已经申请过安全令，请勿重复！")
            return render_template('register.html')

        (pub, pri) = rsa.newkeys(512)
        pub = pub.save_pkcs1()
        pri = pri.save_pkcs1()
        data.loc[len(data)] = (str(id), name, status,
                               "Null", base64.b64encode(pri).decode())
        data.to_csv("user.csv", index=False)
        with open("./keys/"+status+name+str(id)+".pem", "wb") as f:
            f.write(pub)
        
        with open("./keys/"+status+name+str(id)+".phe", "w") as f:
            f.write(json.dumps({"p": str(private_phe.p),
                                "q": private_phe.q}))
        
        flash("成功向教务发送申请！请等待相关人员下发安全令文件。")
        return render_template('register.html')

    return render_template('register.html')
