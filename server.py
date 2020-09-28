
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Bryan",
        "age": 40,
        "occupation": "Senior Software Engineer"
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


class Users(Resource):
    def get( self ):
        return users, 200

class User( Resource ):

    def get(self,name):
        if name is None:
            return users, 200
        for user in users:
            if ( name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        # POST may not create duplicates
        for user in users:
            if ( name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": int(args["age"]),
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        # if we have this user update them
        for user in users:
            if ( name == user["name"]):
                user["age"] = int(args["age"])
                user["occupation"] = args["occupation"]
                return user, 200

        # otherwise create from scratch
        user = {
            "name": name,
            "age": int(args["age"]),
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self,name):
        global users
        users = [user for user in users if user["name"] != name]
        # this will indicate success even if name is not present
        return "{} is deleted".format(name), 200

api.add_resource(User,"/user/<string:name>")
api.add_resource(Users,"/users")

#app.run(debug=True)
#app.run()
app.run(host='0.0.0.0',port=5000)

