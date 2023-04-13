from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api
from Resourcer import Resourcer
from flasgger import Swagger
from src.services.chatBot import Chatbot

application = Flask(__name__) # call it application
Swagger(application)
api = Api(application)


@application.route("/")
def index_get():
    return render_template("index.html")

@application.route("/micro")
def get_micro():
    return render_template("micro.html")

@application.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    print(userText)
    return Chatbot.chatbot_response(self = Chatbot, msg = userText)

Resourcer(api).add_all()


# use main for local environment, the server will not use it!
if __name__ == '__main__':
    application.run(debug=True)