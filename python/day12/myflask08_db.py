from flask import Flask, request, render_template, redirect, url_for , send_from_directory, jsonify
import pymysql
import json
app = Flask(__name__,static_url_path='', 
            static_folder='static')


@app.route('/emp') 
def emp(): 
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                           db='mypy', charset='utf8')
    curs = conn.cursor()
    sql = "select emp_id,emp_name,emp_gender,emp_addr,emp_tel from emp"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()
    return render_template("emp.html",emplist=rows) 


@app.route('/emp_insert.ajax', methods=['POST']) 
def ajax_emp_insert():
    data =request.get_json()
    print(data)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                            db='mypy', charset='utf8')
    
    curs = conn.cursor()
    
    sql = """insert into emp(emp_id,emp_name,emp_gender,emp_addr,emp_tel) values (%s, %s, %s, %s, %s)"""
             
    cnt = curs.execute(sql, (data['emp_id'],data['emp_name'],data['emp_gender'],data['emp_addr'],data['emp_tel']) )
    conn.commit()
    print(cnt)
    return jsonify(msg="okay")


@app.route('/emp_update.ajax', methods=['POST']) 
def ajax_emp_update():
    data =request.get_json()
    print(data)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                            db='mypy', charset='utf8')
    
    curs = conn.cursor()
    
    sql = """update emp set emp_name = %s, emp_gender = %s, emp_addr = %s ,emp_tel = %s where emp_id= %s """
             
    cnt = curs.execute(sql, (data['emp_name'],data['emp_gender'],data['emp_addr'],data['emp_tel'],data['emp_id']))
    conn.commit()
    print(cnt)
    return jsonify(msg="okay")


@app.route('/emp_delete.ajax', methods=['POST']) 
def ajax_emp_delete():
    data =request.get_json()
    print(data)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                            db='mypy', charset='utf8')
    
    curs = conn.cursor()
    
    sql = """delete from emp where emp_id= %s """
             
    cnt = curs.execute(sql, (data['emp_id']))
    conn.commit()
    print(cnt)
    return jsonify(msg="okay")

if __name__ == '__main__': 
    app.run(debug=True, port=80)

