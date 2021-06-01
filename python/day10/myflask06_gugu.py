from flask import Flask, request, render_template, redirect, url_for, jsonify, json
app = Flask(__name__)

@app.route('/gugudan') 
def gugudan(): 
    
    dan = request.args.get("dan")
    
    return render_template("gugudan.html",mygugudan=int(dan)) 

if __name__ == '__main__': 
    app.run(debug=True, port=80)

