# app.py
# render_templateを追加
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', message="こんにちは")


@app.route("/page1")
def page1():
    return render_template('page1.html', message = "Hello")

@app.route('/page2')
def gettest():
    user = request.args.get("user", "Mr. Who")
    msg = request.args.get("msg", "No Message")
    return render_template('page2.html', user=user ,message=msg)

@app.route('/page3')
def posttest():
    return render_template('page3.html')

@app.route('/get_post', methods=['POST'])
# methodsにPOSTを指定すると、POSTリクエストを受けられる
def get_post():
    # request.formにPOSTデータがある
    user = request.form["user"]
    msg = request.form["msg"]
    return render_template('page3.html', user=use, msg=msg)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

