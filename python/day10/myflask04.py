from flask import Flask, request, render_template, redirect, url_for 
app = Flask(__name__)

@app.route('/forward') 
def forward(): 
    return render_template("forward.html") 

if __name__ == '__main__': 
    app.run(debug=True, port=80)

