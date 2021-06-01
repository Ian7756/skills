from flask import Flask, request, render_template, redirect, jsonify
import pymysql
import json
app = Flask(__name__,static_url_path='', 
            static_folder='static')

@app.route('/ajax', methods=['POST']) 
def ajax():
    data =request.get_json()
    print(data)
    return jsonify(result = "success", result2= data)


if __name__ == '__main__': 
    app.run(debug=True, port=80)

