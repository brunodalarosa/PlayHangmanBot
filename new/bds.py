#-*- coding: utf-8 -*-
#Arquivo gerenciador de dados do banco de dados (NDB)

#Google NDB
from google.appengine.ext import ndb

from random import shuffle
import datetime

class Data(ndb.Model):
    chats       = ndb.StringProperty(indexed = False, repeated = True)
    chosen_cats = ndb.IntegerProperty(indexed = False, repeated = True)
    games       = ndb.IntegerProperty(indexed = False)
    day_games   = ndb.IntegerProperty(indexed = False)
    ptBR        = ndb.IntegerProperty(indexed = False)
    enUS        = ndb.IntegerProperty(indexed = False)
    hbIL        = ndb.IntegerProperty(indexed = False)
    n_players   = ndb.IntegerProperty(indexed = False)
    wins        = ndb.IntegerProperty(indexed = False)
    loses       = ndb.IntegerProperty(indexed = False)

class Shout(ndb.Model):
    text    = ndb.StringProperty(indexed = False)
    pos     = ndb.IntegerProperty(indexed = False)
    enabled = ndb.BooleanProperty(indexed = False, default = False)

class User(ndb.Model):
    id    = ndb.StringProperty()
    name  = ndb.StringProperty()
    score = ndb.IntegerProperty()

class ChatInfo(ndb.Model):
    enabled   = ndb.BooleanProperty(indexed = False, default = False)
    rank      = ndb.StructuredProperty(User, repeated = True)
    language  = ndb.StringProperty(indexed = False, default = 'enUS')
    block     = ndb.IntegerProperty(indexed = False, default = -1) #block usage: -1 = welcome message / 0 = main menu / 1 = Config block / 2 = Cat Config block / 3 = pre-game block / 4 = in-game.
    cats      = ndb.IntegerProperty(indexed = False, repeated = True)

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
