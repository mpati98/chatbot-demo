from src.services.UpperName import UpperName
from src.services.chatBot import Chatbot
from flask import request
# A mapping route setter
class Resourcer:

    def __init__(self, api):
        self.api = api

    # def get_microphone(self):
    #     self.api.add_resource(getMicrophone, "/micro")

    def add_all(self):
        self.api.add_resource(UpperName, "/upper")

    # def get_bot_response(self):
    #     userText = request.args.get('msg')
    #     self.api.add_resource(Chatbot.chatbot_response(userText), "/get") 