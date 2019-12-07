
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Bryan",
        "age": 40,
        "occupation": "Technical Lead"
    },
    {
        "name": "Matt",
        "age": 51,
        "occupation": "Architect"
    },
    {
        "name": "Bob",
        "age": 55,
        "occupation": "Senior Software Engineer"
    }
]

class User( Resource ):
    def get(self,name):
        pass
    def post(self,name):
        pass
    def put(self,name):
        pass
    def delete(self,name):
        pass

api.add_resource(User,"/user/<string:name>")
app.run(debug=True)

