import StringIO
import json
import logging
import random
import urllib
import urllib2

# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

TOKEN = '105794279:AAEZQkZX-HnXHMBG8NHkc0CWyDjvpOnHM-U'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


# ========= Classe Enable no ndb. (Do esqueleto)

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

# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']
        #id do guilherme 29942340
        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)

        if text.startswith('/'):
            if text == '/start' or text == '/start@ccuem_bot': #Start
                reply('Bot dos mano ligado')
                setEnabled(chat_id, True)
            elif text == '/stop' or text == '/stop@ccuem_bot': #Stop
                reply('Bot dos mano desligado')
                setEnabled(chat_id, False)
            elif text == '/tio' or text == '/tio@ccuem_bot': #Tio
                reply('diodo')
            elif text == '/bomdia' or text == '/bomdia@ccuem_bot': #Bomdia
                reply('bomdia circuitinhos')
            elif text == '/setcaccom_open' or text == '/setcaccom_open@ccuem_bot': #SetCaccomOpen
                 reply('Voce abriu o Caccom')
                 setCaccom(True)
            elif text == '/setcaccom_close' or text == '/setcaccom_close@ccuem_bot': #SetCaccomClose
                 reply('Voce fechou o caccom')
                 setCaccom(False)
            elif text == '/getcaccom' or text == '/getcaccom@ccuem_bot': #GetCaccom
                caccom = getCaccom()
                if caccom:
                    reply('O caccom ta aberto cara :D')
                else:
                    reply('Caccom fechado, idiota.')
            elif text == '/image': #Gera imagem (código do esqueleto)
                img = Image.new('RGB', (512, 512))
                base = random.randint(0, 16777216)
                pixels = [base+i*j for i in range(512) for j in range(512)]  # generate sample image
                img.putdata(pixels)
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                reply(img=output.getvalue())
            else:
                reply('mano vc eh burro')

        # Aqui estão os algoritmos para as respostas sem serem comandos.

        elif 'who are you' in text:
            reply('telebot starter kit, created by yukuku: https://github.com/yukuku/telebot')
        elif 'what time' in text:
            reply('look at the top-right corner of your screen!')
        elif 'O que cai na prova' in text:
            reply('Suas lagrimas')
        elif '888' in text:
            reply('CALA BOCA OU FILHO DA PUTA QUE DA DDOS')
        else:
            if getEnabled(chat_id):
                try:
                    resp1 = json.load(urllib2.urlopen('http://www.simsimi.com/requestChat?lc=en&ft=1.0&req=' + urllib.quote_plus(text.encode('utf-8'))))
                    back = resp1.get('res')
                except urllib2.HTTPError, err:
                    logging.error(err)
                    back = str(err)
                if not back:
                    reply('okay...')
                elif 'I HAVE NO RESPONSE' in back:
                    reply('you said something with no meaning')
                else:
                    reply(back)
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
