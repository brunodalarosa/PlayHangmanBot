#-*- coding: utf-8 -*-
#Arquivo gerenciador de dados do banco de dados (NDB)

#Google NDB
from google.appengine.ext import ndb

from random import shuffle

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
    g = ndb.Key(Game, chat_id).get()
    if chat_id in c.chats:
        c.chats.remove(chat_id)
        c.put()
        e.key.delete()
        s.key.delete()
        if g:
            g.key.delete()
        return
    return

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
    adm_message = ndb.StringProperty(default = 'noAdm')
    rnd = ndb.IntegerProperty(default = 0)
    palavra = ndb.StringProperty(default = 'noPalavra')
    categoria = ndb.StringProperty(default = 'noCategoria')
    mascara = ndb.StringProperty(default = 'noMascara')
    letras = ndb.StringProperty(repeated = True)
    vidas = ndb.IntegerProperty(default = 6)
    vidas_init = ndb.IntegerProperty(default = 6)
    arriscarBlock = ndb.BooleanProperty(indexed = False, default = False)

def checkPalavra(chat_id, text):
    g = ndb.Key(Game, chat_id).get()
    if g:
        if text == g.palavra.lower():
            return True
    return False

def setArriscarBlock(chat_id, opt):
    g = ndb.Key(Game, chat_id).get()
    if g:
        g.arriscarBlock = opt
        g.put()
        return
    return

def getArriscarBlock(chat_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        return g.arriscarBlock
    return False

def getPreGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        return g.pre_game
    return False

def getRound(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.rnd

def setRound(chat_id):
    g = ndb.Key(Game, chat_id).get()
    g.rnd = g.rnd+1 if g.rnd+1 < len(g.u_ids) else 0
    g.put()
    return

def checkRound(chat_id, u_id):
    g = ndb.Key(Game, chat_id).get()
    if g.u_ids[g.rnd] == u_id:
        return True
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
    setAdm(chat_id, u_id, message_id)
    return

def setInGame(chat_id, status):
    g = ndb.Key(Game, chat_id).get()
    g.in_game = status
    g.put()
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

def rmPlayer(chat_id, u_id, message_id):
    g = ndb.Key(Game, chat_id).get()
    if u_id in g.u_ids:
        ind = g.u_ids.index(u_id)
        g.u_ids.pop(ind)
        g.u_names.pop(ind)
        g.message_ids.pop(ind)
        g.put()
        if len(g.u_ids) == 0:
            delGame(chat_id)
            return False
        if checkAdm(chat_id, u_id):
            setAdm(chat_id, g.u_ids[0], g.message_ids[0])
            return 'setAdm'
        return True
    return 'semPlayer'

def getPlayers(chat_id):
    g = ndb.Key(Game, chat_id).get()
    u_ids = []
    u_names = []
    message_ids = []
    for i in range(len(g.u_ids)):
        u_ids.append(g.u_ids[i].encode('utf-8'))
        u_names.append(g.u_names[i].encode('utf-8'))
        message_ids.append(g.message_ids[i].encode('utf-8'))
    return [u_ids, u_names, message_ids]

#Randomizar a lista de participantes
def shufflePlayers(chat_id):
    g = ndb.Key(Game, chat_id).get()
    u_names_shuf = []
    u_ids_shuf = []
    message_ids_shuf = []
    index_shuf = range(len(g.u_ids))
    shuffle(index_shuf)
    for i in index_shuf:
        u_ids_shuf.append(g.u_ids[i])
        u_names_shuf.append(g.u_names[i])
        message_ids_shuf.append(g.message_ids[i])
    g.u_ids = u_ids_shuf
    g.u_names = u_names_shuf
    g.message_ids = message_ids_shuf
    g.put()

def setAdm(chat_id, u_id, message_id):
    g = ndb.Key(Game, chat_id).get()
    g.adm = u_id
    g.adm_message = message_id
    g.put()
    return

def checkAdm(chat_id, u_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        if g.adm == u_id:
            return True
    return False

def getAdm(chat_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        return g.adm_message
    return False

def setCP(chat_id, categoria, palavra):
    g = ndb.Key(Game, chat_id).get()
    g.categoria = categoria
    g.palavra = palavra
    mascara = ''
    for i in range(len(palavra)):
        if palavra[i] == ' ':
            mascara = mascara+' '
        else:
            mascara = mascara+'*'
    g.mascara = mascara
    g.put()
    return

def setVidas(chat_id):
    g = ndb.Key(Game, chat_id).get()
    modVida = len(g.palavra)/5 if len(g.palavra) > 5 else 0
    modVida += len(g.u_ids)-3 if len(g.u_ids) > 4 else 0
    modVida = 9 if modVida > 9 else modVida
    vidas = g.vidas + modVida
    g.vidas = vidas
    g.vidas_init = g.vidas_init + modVida
    g.put()
    return vidas

def menosVida(chat_id):
    g = ndb.Key(Game, chat_id).get()
    g.vidas -= 1
    g.put()

def getVidas(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.vidas

def getVidasInit(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.vidas_init

def getLetras(chat_id):
    g = ndb.Key(Game, chat_id).get()
    letras = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
    for i in range(len(g.letras)):
        for i in range(len(letras)):
            if g.letras[i] in letras[i]:
                letras[i].remove(g.letras[i])
    return letras

def delGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    g.key.delete()
