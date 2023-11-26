from flask import (
    Flask,
    request,
    redirect,
    url_for,
)

import os

from .database import DBMS, DBConfig

dbConfig: DBConfig = {

}
db = DBMS({

})

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)

@app.get('/')
@app.get('/index')
def index():
    return {
        "path": '/',
        'description': 'index route'
    }

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return {
            "path": '/login',
            "message": "This path just accept JSON"
        }
    elif request.method == 'POST':
        pass

    else:
        return {
            "path": '/login',
            "message": "Unsupported method"
        }

@app.route('/addStructure', methods=['POST'])
def addStructure():
    pass

@app.route('/getStructure', methods=['POST'])
@app.route('/getStrucutre/<string:_id>', methods=['GET'])
def getStructure(_id: str):
    if request.method == 'GET' and _id != None:
        return db.FindStrucure(_id)
    elif _id != None:
            return {
                "path": '/getStructure',
                'message': 'Structure not found.'
            }
    else:
        pass

