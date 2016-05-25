#-*- coding: utf-8 -*-
#Classes declaradas a partir da API do telegram

#Standard imports
import json

#Import local
#import bds as bd
#body.get('message') if body.get('message') else body.get('edited_message')
class Hangman (object):
    def __init__(self, message):
        self.message_id       = message['message_id']
        self.from_            = User(message['from'])
        self.chat             = Chat(message['chat'])
        self.reply_to_message = Hangman(message.get('reply_to_message')) if message.get('reply_to_message') else None
        self.text             = message.get('text')
        self.location         = Location(message.get('location')) if message.get('location') else None
        self.left_chat_member = User(message.get('left_chat_member')) if message.get('left_chat_member') else None
        self.chat_info        = None
        self.game             = None

        if self.text:
            #if self.text.startswith('@ccuem_bot'):
            #    self.text = self.text[11:]
            if self.text.startswith('@PlayHangmanBot'):
                self.text = self.text[15:]
            if not self.text.startswith('/admin'):
                self.text = self.text.lower()

    def checkText(self):
        self.text = '/start' if self.text == self.chat_info.language.ligar.lower() else self.text #Tratamento para o caso do /start
        self.text = self.chat_info.language.ajuda.lower() if self.text.startswith('/help') else self.text
        self.text = self.chat_info.language.desligar.lower() if self.text.startswith('/stop') else self.text

    def setChatInfo(self, chat_info):
        self.chat_info = chat_info

    def setGame(self, game):
        self.game = game

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class User(object):
    def __init__(self, user):
        self.id         = user['id']
        self.first_name	= user['first_name']
        self.last_name  = user.get('last_name')
        self.username   = user.get('username')

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Chat(object):
    def __init__(self, chat):
        self.id         = chat['id']
        self.type       = chat['type']
        self.title      = chat.get('title')
        self.username   = chat.get('username')
        self.first_name = chat.get('first_name')
        self.last_name  = chat.get('last_name')

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Location(object):
    def __init__(self,location):
        self.longitude = location['longitude']
        self.latitude  = location['latitude']

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
