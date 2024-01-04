import json
from flask import Flask, request
import mapper
app = Flask(__name__)

@app.route("/",methods=["GET"])
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




# @app.route("/",methods=["GET"])
# def test():
#     return "hello world"


