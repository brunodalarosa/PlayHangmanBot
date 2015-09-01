#Arquivo gerenciador de dados do banco de dados (NDB)

#Google NDB
from google.appengine.ext import ndb

class Chats(ndb.Model):
    chats = ndb.StringProperty(repeated = True)

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

def delChat(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    e = ndb.Key(Enabled, chat_id).get()
    s = ndb.Key(Settings, chat_id).get()
    if chat_id in c.chats:
        c.chats.remove(chat_id)
        c.put()
        e.key.delete()
        s.key.delete()

def getChats():
    c = ndb.Key(Chats, 'chats').get()
    return c.chats

class Enabled(ndb.Model):
    enabled = ndb.BooleanProperty(indexed = False, default = False)

def setEnabled(chat_id, status):
    e = ndb.Key(Enabled, chat_id).get()
    e.enabled = status
    e.put()
    return

def getEnabled(chat_id):
    e = ndb.Key(Enabled, chat_id).get()
    return e.enabled

class Settings(ndb.Model):
    language = ndb.StringProperty(indexed = False, default = 'pt-BR')

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
