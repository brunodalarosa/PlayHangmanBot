import StringIO
from google.appengine.ext import ndb
from PIL import Image

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

#================================

def setCaccom(status): #Abre ou fecha o caccom dependendo do argumento recebido
    es = CaccomStatus.get_or_insert(str(001))
    es.status = status
    es.put()

def getCaccom(): #Retorna o estado atual do caccom
    es = CaccomStatus.get_by_id(str(001))
    if es:
        return es.status
    return False

class Cmd:
    def comandos(self, text, chat_id):
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
                return('O caccom ta aberto cara :D')
            else:
                return('Caccom fechado, idiota.')
        elif text == '/image' or text == '/image@ccuem_bot': #Gera imagem (codigo do esqueleto)
            img = Image.open("iden.jpg")
            output = StringIO.StringIO()
            img.save(output, 'JPEG')
            a = img=output.getvalue()
            return(a)
        elif text.startswith('/meme'): #manda um meme
            if text == '/meme thuglife':
                img = Image.open("thuglife.jpg")
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                a = img=output.getvalue()
                return(a)
            elif text == '/meme duffzila':
                img = Image.open("duffzila.jpg")
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                a = img=output.getvalue()
                return(a)
            elif text == '/meme diofire':
                img = Image.open("diofire.jpg")
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                a = img=output.getvalue()
                return(a)
            elif text == '/meme hacker':
                img = Image.open("hacker.jpg")
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                a = img=output.getvalue()
                return(a)
            elif text == '/meme isdown':
                img = Image.open("isdown.jpg")
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                a = img=output.getvalue()
                return(a)
            elif text == '/meme help':
                a = 'avaibles memes: thuglife, diofire, duffzila, hacker, isdown'
                return(a)
            else: #if user entered an non existing meme
                a = 'there is no meme for this yet, here the avaibles memes: thuglife, diofire, duffzila, hacker, isdown'
                return(a)
        else:
            return('mano vc eh burro')
