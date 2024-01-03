# agent 后端接口文档

项目语言：python
开发框架：flask，sqlite3（数据库模块）
port：5000
## 功能

### 用户登录

api：/user/login
method：post
#### request：json格式
登录用户的用户名密码
```json
{
    "user_name":"Tom",
    "password":"123456"
}
```
#### response：json格式
登录成功：
```json
{
    "password": "123456",
    "state": true,
    "user_id": 4,
    "user_name": "Tom"
}
```
登录失败
```json
{
    "state": false
}

```

### 用户注册

api：/user/register
method：post

#### request：json格式

发送待注册用户的用户名密码，注意用户名需唯一
```json
{
    "user_name":"Ben",
    "password":"123456"
}
```

#### response：json格式

注册成功：
```json
{
    "password": "123456",
    "state": true,
    "user_id": 5,
    "user_name": "Ben"
}
```
注册失败：
原因一般为用户名重复
```json
{
    "state": false
}

```

### 聊天

api：/chat
method: post

#### request：json格式

发送用户的id和用户名，发送当前聊天内容
```json
{
    "user_name":"Ben",
    "user_id": 1,
    "question": "hi"
}
```

#### response：json格式

```json
{
    "reply": "reply",
    "state": true
}
```


## 源码描述

### 项目结构

```
/smart_agent
---/database
------database.db
---server.py
---mapper.py
```
server.py为后端controller功能模块，实现与前端web连接
mapper.py为后端数据层，实现数据库的连接与操作
database文件夹中存放数据库文件