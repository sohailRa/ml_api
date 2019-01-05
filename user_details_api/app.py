from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flast(__name__)
api = Api(app)


users = 
[
	{
		"name": "Alice",
		"age": 23,
		"SIN": "XXX-123-XXX",
		"occupation": "Web Developer"
	},
	{
		"name": "Kevin",
		"age": 33,
		"SIN": "XXX-456-XXX",
		"occupation": "Civil Engineer"
	},
	{
		"name": "Jenna",
		"age": 18,
		"SIN": "XXX-789-XXX",
		"occupation": "Student"
	},
	{
		"name": "David",
		"age": 68,
		"SIN": "XXX-999-XXX",
		"occupation": "Retired"
	}
]

class User(Resource):

	def get(self, name):
		for user in users:
			if(name == user['name']):
				return user, 200
		return "User not found", 404

	def post(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("SIN")
		parser.add_argument("occupation")
		args = parser.parse_args

		for user in users:
			if(name == user["name"]):
				return "User with name {} already exists".format(name), 400

		user = {
		"name": name,
		"age": args["age"],
		"SIN": args["SIN"],
		"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201

	def put(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("SIN")
		parser.add_argument("occupation")
		args = parser.parse_args

		for user in users:
			if(name == user["name"]):
				user["age"]: args["age"],
				user["SIN"]: args["SIN"],
				user["occupation"]: args["occupation"]
				return user, 200

		user = {
		"name": name,
		"age": args["age"],
		"SIN": args["SIN"],
		"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201

	def delete(self, name):
		global users
		users = [user for user in suers if user["name"] != name]
		return "{} is deleted.".format(name), 200


