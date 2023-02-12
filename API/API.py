#!/usr/bin/python3
# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from predictDGA_API import get_prediction

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class API(Resource):
	def get(self):
		args = request.args
		print(args.get("domain"))
		domain = args.get('domain')
		prob, pred = get_prediction(domain)
		return jsonify({"Domain": domain, "IsDGA": 1 if float(prob) >= 0.5 else 0, "Probability": "{:f}".format(prob)})
		# return jsonify(f"domain,isDGA\n{domain},{1 if float(prob)>= 0.5 else 0}")

# adding the defined resources along with their corresponding urls
api.add_resource(API, "/")

# driver function
if __name__ == "__main__":
	print("Usage: curl http://<Server_IP>:5000?domain=<domain_name>")
	app.run(host="0.0.0.0", debug = True)
