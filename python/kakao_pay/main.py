import requests
import json
import urllib.request
import urllib.response
from nltk.util import pr
from flask import Flask, request, render_template, redirect, url_for, jsonify, json
app = Flask(__name__,static_url_path='', static_folder='static')


class Var:
    tid = ""


@app.route("/kakaopay" ,methods=['POST'])
def pay():
    
    data = request.get_json()
    url = "https://kapi.kakao.com/v1/payment/ready"
    
    param = {
        "cid":"TC0ONETIME",
        "partner_order_id":data["partner_order_id"],
        "partner_user_id":data["partner_user_id"],
        "item_name":data["item_name"],
        "quantity":data["quantity"],
        "total_amount": data["total_amount"],
        "vat_amount":data["vat_amount"],
        "tax_free_amount":data["tax_free_amount"],
        "approval_url":"http://localhost/success",
        "fail_url":"http://localhost/fail",
        "cancel_url":"http://localhost/cancel"
        }
     
    header ={
        "Authorization":"KakaoAK 92d6d22ada8931e12553ea9ece919c49",
        "Content-type":"application/x-www-form-urlencoded;charset=utf-8"
        }
     
    r = requests.post(url, headers=header,params=param)
    Var.tid = json.loads(r.text).get('tid')
    
    return json.loads(r.text)

@app.route('/form') 
def form(): 
    return render_template("form.html") 

@app.route('/success') 
def success(): 
    return render_template("success.html") 


@app.route('/success_data',methods=['POST']) 
def success_data(): 
    
    data = request.get_json()
    url = "https://kapi.kakao.com/v1/payment/approve"
    
    param = {
        "cid":"TC0ONETIME",
        "partner_order_id":"partner_order_id",
        "partner_user_id":"partner_user_id",
        "tid":Var.tid,
        "pg_token":data["pg_token"],
        }
     
    header ={
        "Authorization":"KakaoAK 264f05f3fed7373f5956b8a2f1d0435a",
        "Content-type":"application/x-www-form-urlencoded;charset=utf-8"
        }
     
    r = requests.post(url, headers=header,params=param)
    
    
    return json.loads(r.text) 




@app.route('/fail') 
def fail(): 
    return render_template("fail.html") 

@app.route('/cancel') 
def cancel(): 
    return render_template("cancel.html") 
    
if __name__ == "__main__":
    app.run(debug=True,port=80)
    
    
    
    
