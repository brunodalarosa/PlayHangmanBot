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

#Imports nossos
import bds
import comandos as c

#TOKEN do bot no telegram
TOKEN = '105794279:AAEZQkZX-HnXHMBG8NHkc0CWyDjvpOnHM-U'

#URL base para funcionamento do sistema de Webhook
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

#Versão atual
VERSION = '2.a'

#Nossos IDs
creators = ['112228809', '112255461']

#Línguas suportadas
linguas = ['português(br)', 'english(us)']
# ==================================================

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

        #Dados que recebemos do telegram
        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        left_chat_participant = message.get('left_chat_participant')
        new_chat_participant = message.get('new_chat_participant')
        group_chat_created = message.get('group_chat_created')
        date = message.get('date')
        text = message.get('text').encode('utf-8').lower() if message.get('text') else message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = str(chat['id'])
        user_id = message['from']
        u_id = str(user_id.get('id')).encode('utf-8')
        u_name = user_id.get('first_name').encode('utf-8')

        #'Chama' a verificação
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

        #Lê as configurações
        def getLanguage(chat_id):
            s = bds.getSettings(chat_id) #Classe settings
            if s.language == 'ptBR':
                import ptBR as l
                return l
            elif s.language == 'enUS':
                import enUS as l
                return l
            return

        #Aqui começa a lógica principal
        s = bds.getSettings(chat_id)
        l = getLanguage(chat_id)

        text = '/start' if (text == l.ligar.lower()) else text #Tratamento para o caso do /start

        if not s.waiting:
            if '/start' in text:
                reply(c.start(chat_id))
            elif bds.getEnabled(chat_id):
                if l.desligar.lower() in text:
                    reply(c.stop(chat_id))
                elif l.ajuda.lower() in text:
                    reply(c.ajuda(chat_id))
                elif l.rank.lower() in text:
                    reply(c.rank(chat_id))
                elif l.config.lower() in text:
                    reply(c.config(chat_id))
                elif l.novojogo.lower() in text:
                    reply(c.novojogo(chat_id,u_name))
                elif l.voltar.lower() in text:
                    reply(c.voltarMain(chat_id, l.voltar_msg))

                #elif '/adm' in text:
                    #if u_id in creators:
                        #reply(toDict(chat_id, 'vai mandar msg pra todos'))
        else:
            reply(c.changeLanguage(chat_id, text))

app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
