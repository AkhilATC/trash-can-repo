from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def login():
    return render_template('index.html')


@app.route('/gen_report', methods=['POST'])
def gen_report():
    return "cool"


if __name__ == '__main__':
    app.run(debug=True)