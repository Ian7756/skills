from flask import Flask
from flask import request
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/param', methods=['POST'])
def hello():
    a = request.form['a']
    b = request.form['b']

    return "a:"+a+" b:"+b

if __name__ == "__main__":
    app.run(port=80)