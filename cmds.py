import StringIO
from google.appengine.ext import ndb
from PIL import Image
import time
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
    st = time.strftime("%H:%M:%S")
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


def comandos(text, chat_id):
    if text == '/start' or text == '/start@ccuem_bot': #Start
        setEnabled(chat_id, True)
        return('Bot dos mano ligado')
    elif text == '/stop' or text == '/stop@ccuem_bot': #Stop
        setEnabled(chat_id, False)
        return('Bot dos mano desligado')
    elif text == '/tio' or text == '/tio@ccuem_bot': #Tio
        return('diodo')
    elif text == '/bomdia' or text == '/bomdia@ccuem_bot': #Bomdia
        return('bomdia circuitinhos')
    elif text == '/setcaccom_open' or text == '/setcaccom_open@ccuem_bot': #SetCaccomOpen
        setCaccom(True)
        return('Voce abriu o Caccom')
    elif text == '/setcaccom_close' or text == '/setcaccom_close@ccuem_bot': #SetCaccomClose
        setCaccom(False)
        return('Voce fechou o caccom')
    elif text == '/getcaccom' or text == '/getcaccom@ccuem_bot': #GetCaccom
        caccom = getCaccom()
        if caccom:
            return('O caccom ta aberto cara :D\nUltima modificacao: ' + getCaccomHora())
        else:
            return('Caccom fechado, idiota.\nUltima modificacao: ' + getCaccomHora())
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
