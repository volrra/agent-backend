import json
from flask import Flask, request
import mapper

app = Flask(__name__)
headers = {
        "Content-Type": "application/json"
    }
@app.route("/user/login", methods=["POST"])
def login_controller():
    req_body=request.get_json()
    if type(req_body)==str:
        req_body=json.loads(req_body)
    name=req_body['user_name']
    password=req_body['password']
    dao=mapper.Mapper()
    info_list=dao.get_user(name,password)
    res_data=dict()
    res_data["state"]=True
    if info_list==[]:
        res_data["state"]=False
    else:
        res_data["user_id"]=info_list[0][0]

    return res_data
    # response = requests.post("http://192.168.3.113:8185/wg/route/v2/recommend", headers=headers,
    #                                    data=res_data, )
@app.route("/user/register",methods=["POST"])
def register_controller():
    req_body=request.get_json()
    if type(req_body)==str:
        req_body=json.loads(req_body)
    name=req_body["user_name"]
    password=req_body["password"]
    dao=mapper.Mapper()
    ok=dao.check_username(name)
    res_data=dict()
    res_data["state"]=False

    if ok==True:
        id=dao.insert_user(name,password)
        if id is not None:
            res_data["user_id"] = id
            res_data["user_name"]=name
            res_data["password"] = password
            res_data["state"]=True

    return res_data
    # response = requests.post("http://192.168.3.113:8185/wg/route/v2/recommend", headers=headers,
    #                          data=res_data, )

@app.route("/chat",methods=["POST"])
def chat_controller():
    req_body=request.get_json()
    if type(req_body)==str:
        req_body=json.loads(req_body)
    name=req_body['user_name']
    uid=req_body['user_id']
    question=req_body['question']
    res_data=dict()
    res_data["state"]=True

    # code with chating api

    res_data["reply"]="reply"
    return res_data

@app.route("/test",methods=["GET"]
def test():
    return "hello world"



if __name__=="__main__":
    app.run(host="0.0.0.0")
