from flask import Flask, request, render_template, redirect, url_for , send_from_directory, jsonify
import pymysql
import json
app = Flask(__name__,static_url_path='', static_folder='static')


@app.route('/mat') 
def mat(): 
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                           db='mypy', charset='utf8')
    curs = conn.cursor()
    sql = "select mat_id,mat_name,mat_size,dept from mat"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()
    return render_template("mat.html",matlist=rows) 


@app.route('/mat_insert.ajax', methods=['POST']) 
def ajax_mat_insert():
    data =request.get_json()
    print(data)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                            db='mypy', charset='utf8')
    
    curs = conn.cursor()
    
    sql = """insert into mat(mat_id,mat_name,mat_size,dept) values (%s, %s, %s, %s)"""
             
    cnt = curs.execute(sql, (data['mat_id'],data['mat_name'],data['mat_size'],data['dept']) )
    conn.commit()
    print(cnt)
    return jsonify(msg="okay")


@app.route('/mat_update.ajax', methods=['POST']) 
def ajax_mat_update():
    data =request.get_json()
    print(data)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                            db='mypy', charset='utf8')
    
    curs = conn.cursor()
    
    sql = """update mat set mat_name = %s, mat_size = %s, dept = %s  where mat_id= %s """
             
    cnt = curs.execute(sql, (data['mat_name'],data['mat_size'],data['dept'],data['mat_id']))
    conn.commit()
    print(cnt)
    return jsonify(msg="okay")


@app.route('/mat_delete.ajax', methods=['POST']) 
def ajax_mat_delete():
    data =request.get_json()
    print(data)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                            db='mypy', charset='utf8')
    
    curs = conn.cursor()
    
    sql = """delete from mat where mat_id= %s """
             
    cnt = curs.execute(sql, (data['mat_id']))
    conn.commit()
    print(cnt)
    return jsonify(msg="okay")

if __name__ == '__main__': 
    app.run(debug=True, port=80)

