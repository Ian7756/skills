from flask import Flask, request, render_template, redirect, url_for, jsonify, json
app = Flask(__name__)
import pymysql



@app.route('/db') 
def db(): 
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                           db='mypy', charset='utf8')
    curs = conn.cursor()
    sql = "select * from sample"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()
    return render_template("db.html",mydb=rows) 

if __name__ == '__main__': 
    app.run(debug=True, port=80)

