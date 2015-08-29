#Main do forca_bot 2.0
#-*- coding: utf-8 -*-

#Standard imports
import json
import logging
import random
import urllib
import urllib2

#app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

#Importa o BD
import bds

#TOKEN do bot no telegram
TOKEN = '105794279:AAEZQkZX-HnXHMBG8NHkc0CWyDjvpOnHM-U'

#URL base para funcionamento do sistema de Webhook
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

#Versão atual
VERSION = '2.a'

start_text = 'Olá, bem vindo ao Forca Bot, para começar digite /novojogo'
is_ligado = 'Forca Bot já está ligado!'
stop_text = 'Forca Bot desligado'
help_text = 'Estamos sem jogo no momento'
# ==================================================
def toDict(chat_id, text, replyTo = None, replyMarkup = None):
    return dict(chat_id = chat_id, text = text, reply_to_message_id = replyTo, reply_markup = replyMarkup)

def makeKb(kb, resize_keyboard = None, one_time_keyboard = None, selective = None):
    resize_keyboard = resize_keyboard if resize_keyboard else False
    one_time_keyboard = one_time_keyboard if one_time_keyboard else False
    selective = selective if selective else False
    return json.dumps({'keyboard':kb, 'resize_keyboard':resize_keyboard, 'one_time_keyboard':one_time_keyboard, 'selective':selective})

#Metodos que configuram a conexao do telegram com o App Engine
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

        #Função que verifica se o forca_bot foi excluido ou se ele existe no BD
        def verifyBot(left_chat_participant = None, new_chat_participant = None, group_chat_created = None):
            if left_chat_participant:
                first_name = left_chat_participant['first_name'].encode('utf-8')
                if first_name == 'ccuemBot':
                    bds.delChat(chat_id)
                    return
            if new_chat_participant:
                first_name = new_chat_participant['first_name'].encode('utf-8')
                if first_name == 'ccuemBot':
                    bds.checkChat(chat_id)
                    return
            if group_chat_created:
                bds.checkChat(chat_id)
                return
            return

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        left_chat_participant = message.get('left_chat_participant')
        new_chat_participant = message.get('new_chat_participant')
        group_chat_created = message.get('group_chat_created')
        date = message.get('date')
        text = message.get('text').encode('utf-8') if message.get('text') else message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = str(chat['id'])
        user_id = message['from']
        uId = user_id.get('id')
        uName = user_id.get('first_name')
        if new_chat_participant:
            verifyBot(new_chat_participant = new_chat_participant)
        if left_chat_participant:
            verifyBot(left_chat_participant = left_chat_participant)
        if group_chat_created:
            verifyBot(group_chat_created = True)
        if not text:
            logging.info('no text')
            return

        #Função que envia o dict para o Telegram
        def reply(dict = None):
            if dict:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode(dict)).read()
            else:
                logging.error('no msg or img specified')
                resp = None
            logging.info('send response:')
            logging.info(resp)
<<<<<<< HEAD

        if '/start' in text:
            if bds.getEnabled(chat_id):
                reply(toDict(chat_id, is_ligado))
            else:
                bds.setEnabled(chat_id, True)
                bds.checkChat(chat_id)
                kb = [['/start', '/stop'],['/help', '/rank']]
                keyboard = makeKb(kb, one_time_keyboard=True)
                print keyboard
                reply(toDict(chat_id, start_text, replyMarkup = keyboard))
        elif '/stop' in text:
            bds.setEnabled(chat_id, False)
            reply(toDict(chat_id, stop_text))
        elif bds.getEnabled(chat_id):
            if '/help' in text:
                #if ingame
                reply(toDict(chat_id, help_text))
                #if...
            elif '/rank' in text:
                reply(toDict(chat_id, 'Sem rank'))
=======
        get = cmds.getEnabled
        cc = cmds.comandos #calls the Cmd class
        if text.startswith('/start') or text.startswith('/stop'):
            rpl = cc(text, chat_id, uId)
            reply(rpl)
        else:
            if get(chat_id):
                if text.startswith('/'):
                    if text.startswith('/meme') or text.startswith('/image'):
                        rpl = cc(text, chat_id, uId)
                        if rpl.startswith('O comando') or rpl.startswith('Esse meme'):
                            reply(rpl)
                        else:
                            reply(img=rpl)
                    else:
                        rpl = cc(text, chat_id, uId)
                        reply(rpl)
                else:
                    cc = conversa.responde
                    rpl = cc(text)
                    reply(rpl)
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))
>>>>>>> ee01302ee7b301c907e7457acc1441dc6bb668c6

app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
