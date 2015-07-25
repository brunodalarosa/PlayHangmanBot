import StringIO
from google.appengine.ext import ndb
from PIL import Image
import datetime
#============= ndb do /start ou /stop

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)

# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False

#======= Classe Caccom no ndb. Criado para o funcionamento do sistema Caccom

class CaccomStatus(ndb.Model):
    status = ndb.BooleanProperty(indexed=False, default=False)
    timestamp = ndb.StringProperty(indexed=False, default=False)

#================================

def setCaccom(status): #Abre ou fecha o caccom dependendo do argumento recebido
    time = datetime.datetime.now()
    h = int(time.hour)
    h = h-3
    if(h < 0):
        if h == -1:
            h = 23
        elif h == -2:
            h == 22
        elif h == -3:
            h == 21
    m = str(time.minute)
    s = str(time.second)
    h = str(h)
    st = h+':'+m+':'+s
    es = CaccomStatus.get_or_insert(str(001))
    es.status = status
    es.timestamp = st
    es.put()

def getCaccom(): #Retorna o estado atual do caccom
    es = CaccomStatus.get_by_id(str(001))
    if es:
        return es.status
    return False

def getCaccomHora():
    es = CaccomStatus.get_by_id(str(001))
    return es.timestamp


def comandos(text, chat_id, uId):
    auth = False
    if (uId == 109554359) or  (uId == 112255461) or (uId == 112228809):
        auth = True
    if text == '/start' or text == '/start@ccuem_bot': #Start
        if auth:
            setEnabled(chat_id, True)
            return('Bot Ccuem ligado :D')
        else:
            return('Voce nao tem autorizacao pra fazer isso.')
    elif text == '/stop' or text == '/stop@ccuem_bot': #Stop
        if auth:
            setEnabled(chat_id, False)
            return('Bot Ccuem desligado D:')
        else:
            return('Voce nao tem autorizacao pra fazer isso.')
    elif text == '/setcaccom_open' or text == '/setcaccom_open@ccuem_bot': #SetCaccomOpen
        if auth:
            setCaccom(True)
            return('Voce abriu o Caccom')
        else:
            return('Voce nao tem autorizacao pra fazer isso.')
    elif text == '/setcaccom_close' or text == '/setcaccom_close@ccuem_bot': #SetCaccomClose
        if auth:
            setCaccom(False)
            return('Voce fechou o caccom')
        else:
            return('Voce nao tem autorizacao pra fazer isso.')
    elif text == '/getcaccom' or text == '/getcaccom@ccuem_bot': #GetCaccom
        caccom = getCaccom()
        if caccom:
            return('O caccom ta aberto cara :D\nUltima modificacao: ' + getCaccomHora())
        else:
            return('Caccom fechado, idiota.\nUltima modificacao: ' + getCaccomHora())
    elif text == '/tio' or text == '/tio@ccuem_bot': #Tio
        return('Bom dia, diogo tinha um pacotinho de diodinhos, sabe o que ele fez? Montou um circuitinho!')
    elif text == '/image' or text == '/image@ccuem_bot': #Gera imagem (codigo do esqueleto)
        img = Image.open("images/iden.jpg")
        output = StringIO.StringIO()
        img.save(output, 'JPEG')
        a = img=output.getvalue()
        return(a)
    elif text.startswith('/meme'): #manda um meme
        if text == '/meme thuglife':
            img = Image.open("images/memes/thuglife.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme duffzila':
            img = Image.open("images/memes/duffzila.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme diofire':
            img = Image.open("images/memes/diofire.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme hacker':
            img = Image.open("images/memes/hacker.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme isdown':
            img = Image.open("images/memes/isdown.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme lsd':
            img = Image.open("images/memes/lsd.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme roladream':
            img = Image.open("images/memes/roladream.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text == '/meme help' or text == '/meme h':
            a = 'O comando meme requer apenas um argumento, use /meme NomeDoMeme\nLista de Memes disponiveis:\nthuglife\ndiofire\nduffzila\nhacker\nisdown\nroladream\nlsd\n V -0.1.1lol'
            return(a)
        else: #if user entered an non existing meme
            a = 'Esse meme nao existe ainda! Para uma lista dos memes disponiveis use /meme h ou /meme help'
            return(a)
    else:
        return('mano vc eh burro')
