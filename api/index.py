import json
from flask import Flask, request
import mapper
app = Flask(__name__)

@app.route("/user/login", methods=["GET"])
def login_controller():

    name=request.args.get('user_name')
    password=req_body('password')
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
@app.route("/r",methods=["GET"])
def register_controller():
    name=request.args.get('user_name')
    password=request.args.get('password')
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

    return json.dumps(res_data)
    # response = requests.post("http://192.168.3.113:8185/wg/route/v2/recommend", headers=headers,
    #                          data=res_data, )


@app.route("/chat",methods=["GET"])
def chat_controller():
    name=request.args.get('user_name')
    uid=request.args.get('user_id')
    question=request.args.get('question')
    res_data=dict()
    res_data["state"]=True

    # code with chating api

    res_data["reply"]="reply"
    return res_data

# @app.route("/",methods=["GET"])
# def test():
#     return "hello world"


