from flask import Flask, request, render_template, redirect, url_for, jsonify, json
app = Flask(__name__)

@app.route('/setAttr') 
def setAttr(): 
    params = [
                [1,2],
                [3,4]
            ]
    return render_template("setAttr.html",mylist=params) 

if __name__ == '__main__': 
    app.run(debug=True, port=80)

