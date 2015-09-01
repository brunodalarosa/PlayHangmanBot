#Arquivo gerenciador de dados do banco de dados (NDB)

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
