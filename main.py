#-*- coding: utf-8 -*-
#Main do forca_bot 2.0

#Standard imports
import json
import logging
import random
import urllib
import urllib2
import time

#app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

#Imports nossos
import bds
import comandos as c
import preGame as p
import game as g

#TOKEN TESTE: 105794279:AAEZQkZX-HnXHMBG8NHkc0CWyDjvpOnHM-U
#TOKEN BOT REAL: 130009542:AAHNWctXOV5L_BPf7TTnFTgmQi6O7zD89Rw ***SÓ MUDAR DEPOIS DE TESTAR TODOS OS BUGS***
#TOKEN do bot no telegram
TOKEN = '130009542:AAHNWctXOV5L_BPf7TTnFTgmQi6O7zD89Rw'

#URL base para funcionamento do sistema de Webhook
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

#Versão atual
VERSION = '1.0'

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
        def verifyBot(left_chat_participant = None):
            if left_chat_participant:
                first_name = left_chat_participant['first_name'].encode('utf-8')
                if first_name == 'The Hangman':
                    bds.delChat(chat_id)
                    return
            return

        #Dados que recebemos do telegram
        update_id = body['update_id']
        message = body['message']
        message_id = str(message.get('message_id')).encode('utf-8')
        left_chat_participant = message.get('left_chat_participant')
        new_chat_participant = message.get('new_chat_participant')
        group_chat_created = message.get('group_chat_created')
        date = message.get('date')
        text = message.get('text').encode('utf-8') if message.get('text') else message.get('text')
        if text:
            if not text.startswith('/admin'):
                text = text.lower()
        fr = message.get('from')
        chat = message['chat']
        chat_id = str(chat['id'])
        user_id = message['from']
        u_id = str(user_id.get('id')).encode('utf-8')
        u_name = user_id.get('first_name').encode('utf-8')
        bds.checkChat(chat_id)

        #'Chama' a verificação
        if left_chat_participant:
            verifyBot(left_chat_participant = left_chat_participant)

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
            if s:
                if s.language == 'ptBR':
                    import ptBR as l
                    return l
                elif s.language == 'enUS':
                    import enUS as l
                    return l
            else:
                bds.checkChat(chat_id)
                s = bds.getSettings(chat_id) #Classe settings
                if s.language == 'ptBR':
                    import ptBR as l
                    return l
                elif s.language == 'enUS':
                    import enUS as l
                    return l
                return


        #Aqui começa a lógica principal
        l = getLanguage(chat_id)
        s = bds.getSettings(chat_id)
        ab = bds.getArriscarBlock(chat_id)
        first = bds.getFirstWelcome(chat_id)[0]
        rpl = [c.toDict(chat_id, l.sorry_msg)]
        text = '/start' if text == l.ligar.lower() else text #Tratamento para o caso do /start
        text = l.ajuda.lower() if text.startswith('/help') else text
        text = l.desligar.lower() if text.startswith('/stop') else text
        if text.startswith('@PlayHangmanBot'):
            text = text[15:]
        if (u_id in creators) and (text.startswith('/admin')): #Funções especiais dos criadores do bot
            if text.startswith('/admindelchat'):
                chat = text[14:]
                if len(chat) > 0:
                    if bds.delChat(chat):
                        rpl = [c.toDict(chat_id, 'Chat '+chat+' deletado')]
                    else:
                        rpl = [c.toDict(chat_id, 'Chat '+chat+' não existe')]
            elif text.startswith('/adminshout'):
                text = text[12:]
                chats = bds.getChats()
                rpl = []
                for i in range(len(chats)):
                    time.sleep(1)
                    rpl.append(c.toDict(chats[i], text))
            elif text.startswith('/admingetdadoschat'):
                chat = text[19:]
                if len(chat) > 0:
                    dados = bds.getDadosChat(chat)
                    jogos_dia = bds.getJogosDia(chat, date)
                    if dados:
                        rpl = [c.toDict(chat_id, 'Chat '+str(chat)+'\nJogos: '+ str(dados.games)+'\nJogadores: '+str(len(dados.players))+'\nJogos por dia: '+str(jogos_dia)+'\nTop player: '+dados.topPlayer.u_name.encode('utf-8')+'\n\tScore: '+str(dados.topPlayer.u_score)+'\n\tId: '+str(dados.topPlayer.u_id))]
                    else:
                        rpl = [c.toDict(chat_id, 'Chat '+chat+' não existe')]
            elif text.startswith('/admingetdadosglobais'):
                resp = bds.getDadosGlobais(date)
                rpl = [c.toDict(chat_id, 'Chats: '+str(resp[0])+'\nJogadores: '+str(resp[1])+'\nJogos por dia: '+str(resp[2])+'\nJogos: '+str(resp[3]))]
        elif (not s.waiting) or first:
            #comandos que indiferem do estado atual de jogo
            if '/start' in text:
                rpl = c.start(chat_id, u_id, message_id, first)
            elif bds.getEnabled(chat_id):
                if '/kb' in text:
                    rpl = c.kb(chat_id, u_id, message_id)
                elif l.desligar.lower() in text:
                    rpl = c.stop(chat_id)
                elif l.ajuda.lower() in text:
                    rpl = c.ajuda(chat_id)
                elif l.rank.lower() in text:
                    rpl = c.rank(chat_id)
                elif l.config.lower() in text:
                    rpl = c.config(chat_id, message_id)
                elif l.sobre.lower() in text:
                    rpl = c.sobre(chat_id)
                elif l.voltar.lower() in text:
                    rpl = c.voltar(chat_id, l.voltar_msg, message_id, u_id)
                elif l.comandos.lower() in text:
                    rpl = c.comandos(chat_id, message_id, u_id)
                #comandos inGame
                elif bds.getInGame(chat_id):
                    check = bds.checkUid(chat_id, u_id)
                    if l.cancelar_jogo.lower() in text:
                        rpl = g.cancelarJogo(chat_id, u_id)
                    elif check == True:
                        if bds.getArriscarBlock(chat_id):
                            rpl = g.arriscarPalavra2(chat_id, u_id, u_name, message_id, text)
                        elif l.arriscar.lower() in text:
                            rpl = g.arriscarPalavra1(chat_id, u_id, message_id)
                        elif (len(text) == 1) or (text.startswith('@PlayHangmanBot')):
                            if text.startswith('@PlayHangmanBot'):
                                text = text[10:]
                            rpl = g.chutarLetra(chat_id, u_id, message_id, text)
                    elif check == 'rnd':
                        rpl = [c.toDict(chat_id, l.round_errado_msg)]
                    elif check == 'out':
                        rpl = [c.toDict(chat_id, l.fora_msg)]

                #comandos preGame
                elif bds.getPreGame(chat_id):
                    if l.entrar.lower() in text:
                        rpl = p.entrar(chat_id, u_id, u_name, message_id)
                    elif l.sair.lower() in text:
                        rpl = p.sair(chat_id, u_id, u_name, message_id)
                    elif l.fechar_jogo.lower() in text:
                        rpl = p.fecharJogo(chat_id, u_id, message_id, date)
                    elif l.cancelar_jogo.lower() in text:
                        rpl = p.cancelarJogo(chat_id, u_id)
                #se preGame e inGame == False (vide flowchart)
                elif (not bds.getPreGame(chat_id)) and (not bds.getInGame(chat_id)):
                    if l.novojogo.lower() in text:
                        rpl = c.novojogo(chat_id, u_id, u_name, message_id)
        else:
            if l.ajuda.lower() in text:
                rpl = c.ajuda(chat_id)
            else:
                rpl = c.changeLanguage(chat_id, text, message_id, u_id)
        try:
            for i in range(len(rpl)):
                reply(rpl[i])
        except Exception, e:
            print e
            try:
                reply(c.toDict(chat_id, l.error_msg))
            except Exception, e:
                print e
                reply(c.toDict(chat_id, 'Fatal error, contact @cristoferoswald or @bcesarg6.'))

app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
