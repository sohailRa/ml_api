from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flast(__name__)
api = Api(app)


users = [
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
