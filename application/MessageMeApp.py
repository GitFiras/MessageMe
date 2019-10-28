from flask import Blueprint, jsonify, request

from . import db
from .db_models import Messages, Chats

MessageMeApi = Blueprint('MM_api', __name__)

############################## WORKING ##############################
# Load messages
# /api/chats/<chat_id>/messages?user_id=<user_id>
# REST command with manually inserted chat_id=1, user_id=1: GET http://127.0.0.1:5000/MessageMe/chats/1/messages?user_id=1
@MessageMeApi.route('/MessageMe/chats/<chat_id>/messages', methods=['GET'])
def load_message(chat_id):
    user_id = request.args['user_id']
    message_text = request.json
    message = Messages(text=message_text, user_from=user_id, chat_id=chat_id)
    if message is None:
        return 'message has not been found', 404
    return jsonify(messageid=message.message_id, messagetext=message.text), 200

############################## WORKING ##############################
#  Send message to a chat.
# POST /api/chats/<chat_id>/messages?user_id=<user_id>
# REST command with manually inserted chat_id=1, user_id=1: POST http://127.0.0.1:5000/MessageMe/chats/1/messages?user_id=1
@MessageMeApi.route('/MessageMe/chats/<int:chat_id>/messages', methods=['POST'])
def send_message(chat_id):
    user_id = request.args['user_id']
    message_text = request.json['message']
    message = Messages(text=message_text, user_from=user_id, chat_id=chat_id)
    db.session.add(message)
    db.session.commit()
    return jsonify(messageid=message.message_id, messagetext=message.text), 200


############################## WORKING ##############################
# - Get a list of chats
# GET /api/chats?user_id=<user_id>
# REST command with manually inserted user_id=1: GET http://127.0.0.1:5000/MessageMe/chats?user_id=1
@MessageMeApi.route('/MessageMe/chats', methods=['GET'])
def chat_list():
    # user_id = request.args['user_id']
    chats = Chats.query.all()           # list of chats
    # chats = Chats.query.filter(Messages.user_from == user_id).first()      # NOT WORKING!
    chat_json = []
    for chat in chats:
        chat_json.append({"chat_id":chat.chat_id})      # chat_id
        chat_json.append({"chatname":chat.chatname})    # chatname
    return jsonify(chat_json)


############################## WORKING ##############################
# - A HTML home page
#  GET /?user_id=<user_id>
# REST command with manually inserted user_id=1: GET http://127.0.0.1:5000/?user_id=1
@MessageMeApi.route('/?user_id=<user_id>', methods=['GET'])
def homepage(user_id):
    message_text = request.json['message']
    message = Messages(text=message_text, user_from=user_id)
    if message is None:
        return 'message has not been found', 404
    return jsonify(message.to_dict()), 200