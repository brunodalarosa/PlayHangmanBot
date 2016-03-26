#-*- coding: utf-8 -*-
#Arquivo gerenciador de dados do banco de dados (NDB)

#Google NDB
from google.appengine.ext import ndb

from random import shuffle
import datetime

#Entidade que guarda os IDs dos chats
class Chats(ndb.Model):
    chats = ndb.StringProperty(repeated = True)

#Checa a exisencia do chat, se não existir cria todas as entidades necessárias
def checkChat(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    if not c:
        c = Chats(id = 'chats')
        c.put()
        checkChat(chat_id)
    if not (chat_id in c.chats):
        e = Enabled(id = chat_id)
        s = Settings(id = chat_id)
        r = Rank(id = chat_id)
        d = Dados(id = chat_id)
        c.chats.append(chat_id)
        r.put()
        d.put()
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
    d = ndb.Key(Dados, chat_id).get()
    r = ndb.Key(Rank, chat_id).get()
    status = False
    if chat_id in c.chats:
        c.chats.remove(chat_id)
        c.put()
        status = True
    if d:
        d.key.delete()
        status = True
    if e:
        e.key.delete()
        status = True
    if s:
        s.key.delete()
        status = True
    if g:
        g.key.delete()
        status = True
    if r:
        r.key.delete()
        status = True
    return status

#Retorna a lista de todos os chats ativos no momento
def getChats():
    c = ndb.Key(Chats, 'chats').get()
    return c.chats

def checkChatBd(chat_id):
    c = ndb.Key(Chats, 'chats').get()
    e = ndb.Key(Enabled, chat_id).get()
    s = ndb.Key(Settings, chat_id).get()
    d = ndb.Key(Dados, chat_id).get()
    r = ndb.Key(Rank, chat_id).get()
    status = True
    if not e:
        e = Enabled(id = chat_id)
        e.put()
        status = False
    if not s:
        s = Settings(id = chat_id)
        s.put()
        status = False
    if not d:
        d = Dados(id = chat_id)
        d.put()
        status = False
    if not r:
        r = Rank(id = chat_id)
        r.put()
        status = False
    return status

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

class Shout(ndb.Model):
    shout = ndb.StringProperty(indexed = False, default = '')
    pos = ndb.IntegerProperty(indexed = False, default = 0)
    enable = ndb.BooleanProperty(indexed = False, default = False)

def getShout():
    s = ndb.Key(Shout, 'Shout').get()
    if not s:
        s = Shout(id = 'Shout')
        s.put()
        s = ndb.Key(Shout, 'Shout').get()
    if s.enable:
        chats = getChats()
        s.pos = s.pos + 1 if (s.pos + 1) < len(chats) else 0
        if s.pos == 0:
            s.enable = False
        s.put()
        return [chats[s.pos], s.shout, (len(chats) - (s.pos + 1))]
    return None

def setShout(shout):
    s = ndb.Key(Shout, 'Shout').get()
    s.shout = shout
    s.enable = True
    s.put()
    return

def delShout():
    s = ndb.Key(Shout, 'Shout').get()
    s.enable = False
    s.pos = 0
    s.shout = ''
    s.put()

def lessPos():
    s = ndb.Key(Shout, 'Shout').get()
    s.pos = s.pos - 1
    s.put()

#Guarda as configurações de cada chat
class Settings(ndb.Model):
    language = ndb.StringProperty(indexed = False, default = 'enUS')
    waiting = ndb.BooleanProperty(indexed = False, default = True)
    first = ndb.BooleanProperty(indexed = False, default = True)
    welcome = ndb.BooleanProperty(indexed = False, default = True)
    categorias = ndb.BooleanProperty(indexed = False, default = False)
    cats = ndb.IntegerProperty(repeated = True)

def setCats(chat_id,cats):
    s = ndb.Key(Settings, chat_id).get()
    s.cats = cats
    s.categorias = False
    s.put()
    return

def getCats(chat_id):
    s = ndb.Key(Settings, chat_id).get()
    return s.cats

def getFirstWelcome(chat_id):
    s = ndb.Key(Settings, chat_id).get()
    return [s.first,s.welcome]

def setWelcome(chat_id):
    s = ndb.Key(Settings, chat_id).get()
    s.welcome = False
    s.put()

def setFirst(chat_id):
    s = ndb.Key(Settings, chat_id).get()
    s.first = False
    s.put()

#Retorna a "classe" configurações do chat (caso não existir cria uma nova entidade)
def getSettings(chat_id):
    s = ndb.Key(Settings, chat_id).get()
    if s:
        return s
    if checkChat(chat_id):
        checkChatBd(chat_id)
    getSettings(chat_id)

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

def setCategorias(chat_id, state):
    s = ndb.Key(Settings, chat_id).get()
    s.categorias = state
    s.put()
    return

class User(ndb.Model):
    u_id = ndb.StringProperty()
    u_name = ndb.StringProperty()
    u_score = ndb.IntegerProperty()

class Rank(ndb.Model):
    players = ndb.StructuredProperty(User, repeated = True)

def addPlayerRank(chat_id, u_id, u_name):
    r = ndb.Key(Rank, chat_id).get()
    d = ndb.Key(Dados, chat_id).get()
    for i in range(len(r.players)):
        if u_id == r.players[i].u_id:
            return False
    user = User(u_id = u_id, u_name = u_name, u_score = 0)
    d.players.append(user)
    r.players.append(user)
    r.put()
    d.put()
    return True

def getRank(chat_id):
    r = ndb.Key(Rank, chat_id).get()
    d = ndb.Key(Dados, chat_id).get()
    if len(r.players) != 0:
        rank = sorted(r.players, key = lambda players: players.u_score, reverse = True)
        nomes = []
        scores = []
        for i in range(len(rank)):
            nomes.append(rank[i].u_name.encode('utf-8'))
            scores.append(rank[i].u_score)
        r.players = rank
        d.topPlayer = rank[0]
        r.put()
        d.put()
        return [nomes, scores]
    return []

def addScore(chat_id, u_id, score):
    r = ndb.Key(Rank, chat_id).get()
    for i in range(len(r.players)):
        if r.players[i].u_id == u_id:
            r.players[i].u_score += score
    r.put()
    return

class Dados(ndb.Model):
    games = ndb.IntegerProperty(indexed = False, default = 0)
    topPlayer = ndb.StructuredProperty(User, default = User(u_id = 'noID', u_name ='noPlayer', u_score = 0))
    players = ndb.StructuredProperty(User, repeated = True)
    last_att = ndb.IntegerProperty(indexed = False, default = 1)
    jogos_dia = ndb.IntegerProperty(indexed = False, default = 0)

def getDadosChat(chat_id):
    d = ndb.Key(Dados, chat_id).get()
    if d:
        return d
    d = Dados(id = chat_id)
    d.put()
    return False

def getDadosGlobais(date):
    c = ndb.Key(Chats, 'chats').get()
    n_games = 0
    n_players = 0
    jogos_dia = 0
    u_ids = []
    for i in range (len(c.chats)):
        d = ndb.Key(Dados, c.chats[i]).get()
        if not d:
            getDadosChat(c.chats[i])
            d = ndb.Key(Dados, c.chats[i]).get()
        jogos_dia = jogos_dia + getJogosDia(c.chats[i], date)
        n_games += d.games
        for j in range(len(d.players)):
            if not (d.players[j].u_id in u_ids):
                u_ids.append(d.players[j].u_id)
    n_players = len(u_ids)
    return [len(c.chats), n_players, jogos_dia, n_games]

def setJogosDia(chat_id, date):
    d = ndb.Key(Dados, chat_id).get()
    date = int(datetime.datetime.fromtimestamp(date).strftime('%d'))
    if date != d.last_att:
        d.last_att = date
        d.jogos_dia = 0
    d.jogos_dia += 1
    d.put()

def getJogosDia(chat_id, date):
    d = ndb.Key(Dados, chat_id).get()
    date = int(datetime.datetime.fromtimestamp(date).strftime('%d'))
    if d:
        if date != d.last_att:
            return 0
        return d.jogos_dia
    delChat(chat_id)
    return 0

#Contém todos os dados de cada jogo
class Game(ndb.Model):
    pre_game = ndb.BooleanProperty(indexed = False, default = False)
    in_game = ndb.BooleanProperty(indexed = False, default = False)
    u_ids = ndb.StringProperty(repeated = True)
    u_names = ndb.StringProperty(repeated = True)
    message_ids = ndb.StringProperty(repeated = True)
    adm = ndb.StringProperty(default = 'noAdm')
    adm_name = ndb.StringProperty(default = 'noAdm')
    adm_message = ndb.StringProperty(default = 'noAdm')
    rnd = ndb.IntegerProperty(default = 0)
    palavra = ndb.StringProperty(default = 'noPalavra')
    categoria = ndb.StringProperty(default = 'noCategoria')
    mascara = ndb.StringProperty(default = 'noMascara')
    letras = ndb.StringProperty(repeated = True)
    vidas = ndb.IntegerProperty(default = 6)
    vidas_init = ndb.IntegerProperty(default = 6)
    arriscarBlock = ndb.BooleanProperty(indexed = False, default = False)

def getPreGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    if g:
        return g.pre_game
    return False

def getRound(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.rnd

def roundPlus(chat_id):
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
    setAdm(chat_id, u_id, u_name, message_id)
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
        addPlayerRank(chat_id, u_id, u_name)
        g.u_ids.append(u_id)
        g.u_names.append(u_name)
        g.message_ids.append(message_id)
        g.put()
        return True
    return False

def rmPlayer(chat_id, u_id, message_id):
    g = ndb.Key(Game, chat_id).get()
    if not g.pre_game:
        g.rnd = g.rnd-1 if g.rnd != 0 else len(g.u_ids)-1
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
            setAdm(chat_id, g.u_ids[0], g.u_names[0], g.message_ids[0])
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
def shufflePlayers(chat_id, date):
    g = ndb.Key(Game, chat_id).get()
    setJogosDia(chat_id, date)
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

def setAdm(chat_id, u_id, u_name, message_id):
    g = ndb.Key(Game, chat_id).get()
    g.adm = u_id
    g.adm_name = u_name
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
        return [g.adm.encode('utf-8'), g.adm_name.encode('utf-8') ,g.adm_message.encode('utf-8')]
    return False

def setCP(chat_id, categoria, palavra):
    g = ndb.Key(Game, chat_id).get()
    d = ndb.Key(Dados, chat_id).get()
    d.games += 1
    g.categoria = categoria
    g.palavra = palavra#palavra.decode('utf-8')
    mascara = ''
    for i in range(len(g.palavra)):
        if palavra[i] == ' ':
            mascara = mascara+' '
        else:
            mascara = mascara+'*'
    g.mascara = mascara
    g.put()
    d.put()
    return mascara

def getCategoria(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.categoria.encode('utf-8')


def checkPalavra(chat_id, u_id, text):
    g = ndb.Key(Game, chat_id).get()
    if g:
        if text == g.palavra.encode('utf-8').lower():
            addScore(chat_id, u_id, (len(text)*2))
            g.key.delete()
            return True
    return False

def getPalavra(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.palavra

def getMascara(chat_id):
    g = ndb.Key(Game, chat_id).get()
    return g.mascara.encode('utf-8')

def checkUid(chat_id, u_id):
    g = ndb.Key(Game, chat_id).get()
    if u_id in g.u_ids:
        if checkRound(chat_id, u_id):
            return True
        return 'rnd'
    return 'out'

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
    if g.vidas <= 0:
        delGame(chat_id)
        return True
    if g.vidas == 1:
        g.put()
        return 2
    g.put()
    return False

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
        for j in range(len(letras)):
            if g.letras[i].upper() in letras[j]:
                letras[j].remove(g.letras[i].upper())
    return letras

def checkLetra(chat_id, u_id, letra): #Ve claramente que é pura gambiarra!
    g = ndb.Key(Game, chat_id).get()
    chs = ['á','ã','â','é','ê','í','ó','õ','ô','ú','ç'] #Lista de caracteres especiais suportados no momento, NÃO ADICIONAR PALAVRAS COM CARACTERES NÃO SUPORTADOS!
    ch = ['a','a','a','e','e','i','o','o','o','u','c'] #Acompanha o chs para funcionar. Gambiarra.
    for i in range(len(chs)):
        chs[i] = chs[i].decode('utf-8')
        ch[i] = ch[i].decode('utf-8')

    letra.decode('utf-8')
    palavra = g.palavra.lower()
    nPalavra = g.palavra.lower()
    aux = [None] * len(nPalavra)
    for i in range(len(nPalavra)):
        if nPalavra[i] in chs:
            idc = chs.index(palavra[i])
            idx = palavra.index(chs[idc])
            aux[i] = chs[idc]
            nPalavra = nPalavra[:idx] + ch[idc] + nPalavra[idx+1:] #Reconstrói a palavra sem caracteres especiais
    if not (letra in g.letras):
        if letra.lower() in nPalavra.lower():
            nMascara = ''
            score = 0
            for i in range(len(nPalavra)):
                if nPalavra[i].lower() == letra:
                    letraAnt = letra
                    if aux[i]: #Se existem caracteres especiais
                        letra = aux[i]
                    nMascara = nMascara+letra #substitui a letra na posição
                    letra = letraAnt
                    score += 1
                else:
                    nMascara = nMascara+g.mascara[i]
            g.mascara = nMascara
            addScore(chat_id, u_id, (score*2))
            g.letras.append(letra)
            g.put()
            if g.palavra.lower() == nMascara:
                return nMascara.encode('utf-8')
            return True
        g.letras.append(letra)
        g.put()
        return False
    g.put()
    return 2

def delGame(chat_id):
    g = ndb.Key(Game, chat_id).get()
    g.key.delete()
