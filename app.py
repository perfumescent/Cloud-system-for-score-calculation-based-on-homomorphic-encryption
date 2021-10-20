from flask import (
    Flask, render_template, request, flash,
    url_for, redirect, session, make_response
)
from werkzeug.utils import secure_filename
import pandas as pd
import rsa
import base64
from phe import paillier
import json
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
# public_phe, private_phe = paillier.generate_paillier_keypair()
with open("keys/homo.phe", "r") as f:
    js = json.load(f)
public_phe = paillier.PaillierPublicKey(int(js['pub']))
private_phe = paillier.PaillierPrivateKey(
    public_phe, int(js['p']), int(js['q']))


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

        # 明文加密成密文，打包成json
        def f(x):
            cipher = public_phe.encrypt(float(x))
            return json.dumps(
                {'text': str(cipher.ciphertext()),
                 'exponent': cipher.exponent})
        data['mark'] = data['mark'].map(f)

        # 加入课程名和学分，组合成新的表
        data['course'] = [course for i in range(len(data))]
        data['credit'] = [credit for i in range(len(data))]
        data = pd.concat([mark, data])

        data.to_csv("mark.csv", index=False)
        flash(course+" 成绩上传成功！")

    return render_template('upload.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        df = pd.read_csv('mark.csv')
        mark = df[df.id == int(session['id'])]

        def f(x):
            x = json.loads(x)
            return paillier.EncryptedNumber(public_phe, int(x['text']), int(x['exponent']))
        mark['mark'] = mark['mark'].map(f)

        grade = 0
        for i, v in mark['mark'].items():
            # print(private_phe.decrypt(mark.at[i, 'mark']))
            # print(mark.at[i, 'mark'], int(mark.at[i, 'credit']))
            grade += mark.at[i, 'mark'] * int(mark.at[i, 'credit'])
        mark.loc[len(mark)] = ("Final Grade:",
                               grade/mark.credit.sum(),
                               ",".join(mark.course.value_counts().keys()),
                               mark.credit.sum())

        def g(x):
            return json.dumps(
                {'text': str(x.ciphertext()),
                 'exponent': x.exponent})

        mark['mark'] = mark['mark'].map(g)

        out = io.StringIO()
        mark.to_csv(out, index=False)
        file_name = str(session['id']) + '.csv'
        response = make_response(out.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=%s" % file_name
        response.headers["Content-type"] = "text/csv"
        return response

    mark = pd.read_csv('mark.csv')
    flash('您已结算成绩的课程有：'+', '.join(mark.course.value_counts().index))
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

        if status != '教师':
            with open("./keys/"+status+name+str(id)+".phe", "w") as f:
                json.dump({"pub": str(public_phe.n),
                           "p": str(private_phe.p),
                           "q": str(private_phe.q)},
                          f)

        flash("成功向教务发送申请！请等待相关人员下发安全令文件。")
        return render_template('register.html')

    return render_template('register.html')
