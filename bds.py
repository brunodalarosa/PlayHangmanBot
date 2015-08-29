#Arquivo gerenciador de dados do banco de dados (NDB)

#Google NDB
from google.appengine.ext import ndb

class Chats(ndb.Model):
    chats = ndb.StringProperty(repeated=True)

def checkChat(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    if not (chat_id in c.chats):
        c.chats.append(chat_id)
        c.put()
        return True
    return False

def delChat(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    e = ndb.Key(Enabled, chat_id).get()
    if c:
        if chat_id in c.chats:
            c.chats.remove(chat_id)
            c.put()
    if e:
        e.key.delete()

def getChats():
    c = ndb.Key(Chats, 'chats').get()
    return c.chats

class Enabled(ndb.Model):
    enabled = ndb.BooleanProperty(indexed=False)

def setEnabled(chat_id, status):
    e = ndb.Key(Enabled, chat_id).get()
    if e:
        e.enabled = status
        e.put()
        return
    e = Enabled(id = chat_id, enabled = status)
    e.put()

def getEnabled(chat_id):
    e = ndb.Key(Enabled, chat_id).get()
    if e:
        return e.enabled
    e = Enabled(id = chat_id)
    e.put()
    return False
