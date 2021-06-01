from flask import Flask, request, render_template, redirect, url_for , send_from_directory, jsonify
import pymysql
import json
import qrcode

app = Flask(__name__,static_url_path='', static_folder='static')


@app.route('/omock') 
def omock(): 
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                           db='mypy', charset='utf8')
    curs = conn.cursor()
    sql = "select distinct pan from omock"
    curs.execute(sql)
    rows = curs.fetchall()
    
    for i in rows:
        strCode = 'http://192.168.46.28/omock_detail?pan='+str(i[0])
        img = qrcode.make(strCode)
        img.save('static/gibo/'+str(i[0])+'.png')
        
    conn.close()
    return render_template("omock.html",panList=rows) 


@app.route('/omock_detail') 
def omock_detail(): 
    
    pan = request.args.get('pan')
    print(pan)

    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                           db='mypy', charset='utf8')
    curs = conn.cursor()
    sql = """select * from omock where pan = %s """
    curs.execute(sql,pan)
    rows = curs.fetchall()
    conn.close()
    return render_template("omock_detail.html",game=rows) 

if __name__ == '__main__': 
    app.run(debug=True, port=80,host='0.0.0.0')

