import datetime
import json

from bson import json_util
from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo,pymongo
from bson.objectid import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

CONNECTION_STRING = "mongodb+srv://Erich:a@cluster0.xmzt2qs.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('vocacionales')
user_collection = pymongo.collection.Collection(db, 'vocacionales')


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://Erich:a@cluster0.xmzt2qs.mongodb.net/?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = "75490ca4cc474c2b3b8389c863fd0c0d93b6e0af"

mongo = PyMongo(app)


@app.route('/vocacional', methods=['GET'])
def get_vocacional():
    vocacional = user_collection.find()
    return Response(json_util.dumps(vocacional), mimetype='application/json')


@app.route('/vocacional', methods=['POST'])
def createvocacional():
    # recibe la data
    nombre = request.json['username']
    apellido = request.json['apellido']
    if nombre and apellido:
        id = user_collection.insert_one(
            {'username': nombre, 'apellido': apellido}
        )
        response = {
            'id': str(id)
        }
        return response
    else:
        {'message': 'received'}
    return {'mensage': 'received'}


if __name__ == "__main__":
    app.run(debug=True)
