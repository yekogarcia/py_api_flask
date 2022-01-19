from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#Configuración  de base de datos

USER_DB = 'yekog'
PASS_DB = 'yekog'
URL_DB = 'localhost'
NAME_DB = 'flask'

URL = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root@localhost/flaskmysql'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://yekog:yekog@localhost/flask'
app.config["SQLALCHEMY_DATABASE_URI"] = URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)



#Iniciamos el modelo
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

db.create_all()
  
  #Iniciamos los servicios

@app.route('/get-prime-numbers/<int:number>', methods=['GET'])

def prime_numbers(number=0):
    num = int(number)
    numbers = []
    for n in range(1, num):
        if num % n != 0:
            numbers.append(n)
    numbers = " ".join(map(str, numbers))
    print(numbers)
    return  jsonify(numbers)

@app.route('/convert-height', methods=['POST'])

def convert():
    name = request.json['name']
    height = request.json['height']
    height = height * 0.0254
    data = {'name': name ,  'height': height}

    return jsonify(data)

@app.route('/set-data', methods=['PUT'])
def sendData():
    name = request.json['name']
    description = request.json['description']
    data= Test(name, description)

    db.session.add(data)
    db.session.commit()

    result = {"result": True, "msg": "Datos enviados correctamente" }
    return jsonify(result)


@app.route('/', methods=['GET'])
@app.route('/', methods=['POST'])
@app.route('/', methods=['PUT'])
def index():
    params = {
        'message': 'Welcome to my API test',
        "methods":
                {"set-data":
                    {
                        "name": "String",
                        "description": "String",
                        "type": "json",
                        "method": "PUT"
                    },
                "convert-height":
                    {
                        "name": "String",
                        "height": "Integer",
                        "type": "json",
                        "method": "GET"
                    },
                "get-prime-numbers":
                    {
                         "type": "query string"
                    }
                }
            }
    return jsonify(params)

#Control de exepciones
@app.errorhandler(404)
def error404(err):
    error = {"error": "404 Not Found",
    "msg":"The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again"}
    return jsonify(error)

@app.errorhandler(405)
def error405(err):
    error = {"error": "405 Method Not Allowed",
    "msg":"The method is not allowed for the requested URL."}
    return jsonify(error)

if __name__== "__main__":
    app.run(debug=True)