from flask import Flask, request, redirect, render_template, session, flash
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib
import uuid
import re


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)



# トップ画面表示
@app.route('/top')
def top():
    return render_template('registration/top.html')


### ログイン関係はサンプルアプリとほぼ同じです。
# サインアップ
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')


@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email =='' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(uid, name, email, password)
        DBuser = dbConnect.getUser(email)

        if DBuser != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(user)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')


# ログイン
@app.route('/login')
def login():
    return render_template('registration/login.html')


@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email =='' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                return redirect('/')
    return redirect('/login')


# ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



### ここ（９５行目）から１８３行目までが主な変更箇所です。
# map画面を呼び出す
@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
        return redirect('/top')

    else:
        # 全都道府県の情報を取得する。
        prefectures = dbConnect.getPrefectureAll()
    # 下の二つの変数をhtmlに渡す。 
    return render_template('map.html', prefectures=prefectures, uid=uid)



### 都道府県別チャンネル一覧表示機能
@app.route('/pref/<pref_id>')              
def pref(pref_id):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    # IDが一致する都道府県の情報を取得する。
    prefecture = dbConnect.getPrefectureById(pref_id)
    # 都道府県IDが一致する全チャンネルを取得する。
    channels = dbConnect.getChannelByPref(pref_id)
    # 下の三つの変数をhtmlに渡す。
    return render_template('pref.html', prefecture=prefecture, channels=channels, uid=uid)
    



### チャンネル追加機能（モーダル）　 
### これはおそらく不使用。
@app.route('/pref/<pref_id>', methods=['POST'])
def add_channel(pref_id):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)
    if channel == None:
        channel_description = request.form.get('channel-description')

        dbConnect.addChannel(uid, channel_name, channel_description, pref_id)
        
        return redirect(f'/pref/{pref_id}')
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)



### チャンネル追加機能（独立ページ）
@app.route('/create_channel/<pref_id>')
def show_form_create_channel(pref_id):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    
    # 都道府県idが該当する県の情報を取得する。
    prefecture = dbConnect.getPrefectureById(pref_id)
    
    return render_template('create-channel.html', prefecture=prefecture)



### チャンネル追加機能（独立ページ）
@app.route('/create_channel/<pref_id>', methods=['POST'])
def create_channel(pref_id):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    
    #prefecture = dbConnect.getPrefectureById(pref_id)
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)

    if channel == None:
        channel_description = request.form.get('channel-description')

        # 該当する県にチャンネルを追加。
        dbConnect.addChannel(uid, channel_name, channel_description, pref_id)
        # 該当する県のチャンネル一覧ページへ。
        return redirect(f'/pref/{pref_id}')
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)






### 以下、サンプルアプリのままです。追加機能実装後に変更予定。


### チャットルーム 
@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)




###　 チャンネル更新　都道府県は変更しない。
@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')

    dbConnect.updateChannel(uid, channel_name, channel_description, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


### チャンネル削除機能
@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            pref_id = channel["pref_id"]
            prefecture = dbConnect.getPrefectureById(pref_id)
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelByPref(pref_id)
            return render_template('pref.html', prefecture=prefecture, channels=channels, uid=uid)




@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')

    if message:
        dbConnect.createMessage(uid, channel_id, message)

    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)



@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    cid = request.form.get('channel_id')
    if message_id:
        dbConnect.deleteMessage(message_id)

    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)

"""
404.htmlを作成したらコメントアウトを外す。
jinja2.exceptions.TemplateNotFound: error/404.htmlがターミナルに表示されるため。
@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')
@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')
"""

if __name__ == '__main__':
    app.run(debug=True)
