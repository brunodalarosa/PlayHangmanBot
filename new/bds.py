#-*- coding: utf-8 -*-
#Arquivo gerenciador de dados do banco de dados (NDB)

#Google NDB
from google.appengine.ext import ndb

from random import shuffle
import datetime


def criaData():
    data = Data(id = 'data')
    data.put()

def configure(hangman):
    data = ndb.Key(Data, 'data').get()
    if data:
        if (not hangman.chat.id in data.chats) and (not ndb.Key(ChatInfo, hangman.chat.id).get()):
            #Instancia
            chat_info = ChatInfo(id = hangman.chat.id)
            hangman.setChatInfo(chat_info)
            chat_info.put()
        else:
            #lê
            chat_info = ndb.Key(ChatInfo, hangman.chat.id).get()
            hangman.setChatInfo(chat_info)

            #Lê o Game se estiver no pre-game ou ingame
            if hangman.chat_info.block >= 4:
                game = ndb.Key(Game, hangman.chat.id).get()
                hangman.setGame(game)

            hangman.chat_info.getLanguage()
    else:
        criaData()
        configure(hangman)


class Data(ndb.Model):
    chats       = ndb.StringProperty(indexed = False, repeated = True)
    chosen_cats = ndb.IntegerProperty(indexed = False, repeated = True)
    games       = ndb.IntegerProperty(indexed = False, default = 0)
    day_games   = ndb.IntegerProperty(indexed = False, default = 0)
    ptBR        = ndb.IntegerProperty(indexed = False, default = 0)
    enUS        = ndb.IntegerProperty(indexed = False, default = 0)
    hbIL        = ndb.IntegerProperty(indexed = False, default = 0)
    n_players   = ndb.IntegerProperty(indexed = False, default = 0)
    wins        = ndb.IntegerProperty(indexed = False, default = 0)
    loses       = ndb.IntegerProperty(indexed = False, default = 0)

class Shout(ndb.Model):
    text    = ndb.StringProperty(indexed = False)
    pos     = ndb.IntegerProperty(indexed = False)
    enabled = ndb.BooleanProperty(indexed = False, default = False)

def getShout(data):
    shout = ndb.Key(Shout, 'shout').get()
    if not s:
        shout = Shout(id = 'shout')
        shout.put()
        getShout(data)
    if shout.enable:
        shout.pos = shout.pos + 1 if (shout.pos + 1) < len(data.chats) else 0
        if shout.pos == 0:
            shout.enable = False
        shout.put()
        return [data.chats[s.pos], shout.text, (len(data.chats) - (shout.pos + 1))]
    return None


class User(ndb.Model):
    id    = ndb.StringProperty()
    name  = ndb.StringProperty()
    score = ndb.IntegerProperty()

class ChatInfo(ndb.Model):
    enabled   = ndb.BooleanProperty(indexed = False, default = False)
    rank      = ndb.StructuredProperty(User, repeated = True)
    language  = ndb.StringProperty(indexed = False, default = 'enUS')
    block     = ndb.IntegerProperty(indexed = False, default = -1) #block usage: -1 = welcome message / 0 = main menu / 1 = Config block / 2 = Cat Config block / 3 = mode block /4 = pre-game block / 5 = in-game.
    cats      = ndb.IntegerProperty(indexed = False, repeated = True)

    def getLanguage(self):
        if self.language == 'enUS':
            import enUS as l
            self.language = l

        if self.language =='ptBR':
            import ptBR as l
            self.language = l

        if self.language == 'hbIL':
            import hbIL as l
            self.language = l

        if self.language == 'ruRU':
            import ruRU as l
            self.language = l

class Game(ndb.Model):
    u_ids           = ndb.StringProperty(repeated = True)
    u_names         = ndb.StringProperty(repeated = True)
    message_ids     = ndb.StringProperty(repeated = True)
    adm             = ndb.StringProperty(default = 'noAdm')
    adm_name        = ndb.StringProperty(default = 'noAdm')
    adm_message     = ndb.StringProperty(default = 'noAdm')
    round           = ndb.IntegerProperty(default = 0)
    word            = ndb.StringProperty(default = 'noWord')
    cat             = ndb.StringProperty(default = 'noCat')
    mask            = ndb.StringProperty(default = 'noMask')
    letters         = ndb.StringProperty(repeated = True)
    lifes           = ndb.IntegerProperty(default = 6)
    lifes_init      = ndb.IntegerProperty(default = 6)
    block           = ndb.BooleanProperty(indexed = False, default = False)
