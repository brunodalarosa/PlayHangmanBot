#-*- coding: utf-8 -*-
#Arquivo gerenciador de dados do banco de dados (NDB)

#TODO
#Transformar em structured property

#Google NDB
from google.appengine.ext import ndb

#Entidade que guarda os IDs dos chats
class Chats(ndb.Model):
    chats = ndb.StringProperty(repeated = True)

#Checa a exisencia do chat, se não existir cria todas as entidades necessárias
def checkChat(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    if not (chat_id in c.chats):
        e = Enabled(id = chat_id)
        s = Settings(id = chat_id)
        c.chats.append(chat_id)
        e.put()
        s.put()
        c.put()
        return False
    return True

#Remove o chat e todas as suas dependências
def delChat(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    e = ndb.Key(Enabled, chat_id).get()
    s = ndb.Key(Settings, chat_id).get()
    if chat_id in c.chats:
        c.chats.remove(chat_id)
        c.put()
        e.key.delete()
        s.key.delete()

#Retorna a lista de todos os chats ativos no momento
def getChats():
    c = ndb.Key(Chats, 'chats').get()
    return c.chats

#Guarda o estado de "ligado" e "deligado" de cada chat
class Enabled(ndb.Model):
    enabled = ndb.BooleanProperty(indexed = False, default = False)

#Grava o dado recebido como parâmetro, todos os 'sets' serão assim
def setEnabled(chat_id, status):
    e = ndb.Key(Enabled, chat_id).get()
    e.enabled = status
    e.put()
    return

#Retorna o estado atual do chat
def getEnabled(chat_id):
    e = ndb.Key(Enabled, chat_id).get()
    return e.enabled

#Guarda as configurações de cada chat
class Settings(ndb.Model):
    language = ndb.StringProperty(indexed = False, default = 'ptBR')
    waiting = ndb.BooleanProperty(indexed = False, default = False)

#Retorna a "classe" configurações do chat (caso não existir cria uma nova entidade)
def getSettings(chat_id):
    s = ndb.Key(Settings, chat_id).get()
    if s:
        return s
    checkChat(chat_id)
    s = ndb.Key(Settings, chat_id).get()
    return s

def setLanguage(chat_id, language):
    s = ndb.Key(Settings, chat_id).get()
    s.language = language
    s.put()
    return

def setWaiting(chat_id, waiting):
    s = ndb.Key(Settings, chat_id).get()
    s.waiting = waiting
    s.put()
    return

#Contém todos os dados de cada jogo
class Game(ndb.Model):
    pre_game = ndb.BooleanProperty(indexed = False, default = False)
    in_game = ndb.BooleanProperty(indexed = False, default = False)
    u_ids = ndb.StringProperty(repeated = True)
    u_names = ndb.StringProperty(repeated = True)
    message_ids = ndb.StringProperty(repeated = True)
    adm = ndb.StringProperty(default = 'noAdm')
    rnd = ndb.IntegerProperty(default = 0)
    palavra = ndb.StringProperty(default = 'noPalavra')
    dica = ndb.StringProperty(default = 'noDica')
    mascara = ndb.StringProperty(default = 'noMascara')
    letras = ndb.StringProperty(repeated = True)
    vidas = ndb.IntegerProperty(default = 6)
    vidas_init = ndb.IntegerProperty(default = 6)

def getPreGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        return g.pre_game
    return False

def setPreGame(chat_id, status, u_id = None, u_name = None, message_id = None):
    g = ndb.Key(Game, chat_id).get()
    if g:
        g.pre_game = status
        g.put()
        return
    g = Game(id = chat_id)
    g.put()
    g = ndb.Key(Game, chat_id).get()
    g.pre_game = status
    g.put()
    addPlayer(chat_id, u_id, u_name, message_id)
    setAdm(chat_id, u_id)
    return

def setInGame(chat_id, status):
    g = ndb.Key(Game, chat_id).get()
    g.in_game = status
    return

def getInGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        return g.in_game
    return False

def addPlayer(chat_id, u_id, u_name, message_id):
    g = ndb.Key(Game, chat_id).get()
    if not (u_id in g.u_ids):
        g.u_ids.append(u_id)
        g.u_names.append(u_name)
        g.message_ids.append(message_id)
        g.put()
        return True
    return False

def setAdm(chat_id, u_id):
    g = ndb.Key(Game, chat_id).get()
    g.adm = u_id
    g.put()
    return

def checkAdm(chat_id, u_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        if g.adm == u_id:
            return True
    return False

def delGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    g.key.delete()
