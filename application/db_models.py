from . import db
import datetime

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.Time, index=True, default=datetime.datetime.utcnow)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Userschats(db.Model):
    user_chat_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Time,index=True, default=datetime.datetime.utcnow)
    users_userid = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    chats_chatid = db.Column(db.Integer, db.ForeignKey('chats.chat_id'))

class Chats(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    chatname = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

class Messages(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    text = db.Column(db.String(256))
    user_from = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.chat_id'))

    @staticmethod
    def from_dict(dict):
        return Messages(id=dict.get('id'), name=dict['name'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'  : self.id,
           'name': self.name,
       }