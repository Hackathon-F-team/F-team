from flask import Flask


# Flaskクラスのインスタンスappを作成する。
app = Flask(__name__)


# "/"にGETメソッドでアクセスがあった場合、hello()を呼び出し、'<h1>Hello World!</h1>'を表示する。
@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'


#　このモジュールを実行した場合、app.run()を実行し、デバッグモードでサーバーを立ち上げる。
if __name__ == '__main__':
    app.run(debug=True)