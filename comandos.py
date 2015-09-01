#-*- coding: utf-8 -*-
#Arquivo com as funções dos comandos executados (melhorar)

#Standard imports
import json
import bds

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

#Recebe os dados que serão repondidos e transforma em um dict
def toDict(chat_id, text, replyTo = None, replyMarkup = None):
    return dict(chat_id = chat_id, text = text, reply_to_message_id = replyTo, reply_markup = replyMarkup)

#Recebe uma matriz e a tranforma em um teclado personalizado
def makeKb(kb, resize_keyboard = None, one_time_keyboard = None, selective = None):
    resize_keyboard = resize_keyboard if resize_keyboard else False
    one_time_keyboard = one_time_keyboard if one_time_keyboard else False
    selective = selective if selective else False
    return json.dumps({'keyboard':kb, 'resize_keyboard':resize_keyboard, 'one_time_keyboard':one_time_keyboard, 'selective':selective})

def inicial_kb(chat_id):
    l = getLanguage(chat_id)
    return [[l.novojogo], [l.ligar, l.desligar], [l.ajuda, l.rank], [l.config]] #possíveis keyboards


#Funções dos comandos
def start(chat_id):
    l = getLanguage(chat_id)
    if bds.getEnabled(chat_id):
        return toDict(chat_id, l.is_enabled)
    bds.setEnabled(chat_id, True)
    bds.checkChat(chat_id)
    l = getLanguage(chat_id)
    keyboard = makeKb(inicial_kb(chat_id), one_time_keyboard = True)
    return toDict(chat_id, l.start_msg, replyMarkup = keyboard)

def stop(chat_id):
    l = getLanguage(chat_id)
    bds.setEnabled(chat_id, False)
    return toDict(chat_id, l.stop_msg)

def ajuda(chat_id):
    l = getLanguage(chat_id)
    #Vai enviar ajuda dependendo do estado de jogo
    return toDict(chat_id, l.start_help_msg)

def rank(chat_id):
    l = getLanguage(chat_id)
    #Vai enviar ajuda dependendo do estado de jogo
    return toDict(chat_id, 'Sem rank')

def novojogo(chat_id, u_name):
    l = getLanguage(chat_id)
    keyboard = makeKb([[l.voltar]], one_time_keyboard = True)
    return toDict(chat_id, l.inicialMsg(u_name), replyMarkup = keyboard)

def voltarMain(chat_id, msg):
    keyboard = makeKb(inicial_kb(chat_id), one_time_keyboard = True)
    return toDict(chat_id, msg, replyMarkup = keyboard )

def config(chat_id):
    l = getLanguage(chat_id)
    language_kb = [['Português(BR)', 'English(US)'], [l.voltar]]
    bds.setWaiting(chat_id, True)
    keyboard = makeKb(language_kb, one_time_keyboard = True)
    return toDict(chat_id, l.linguas, replyMarkup = keyboard)

def changeLanguage(chat_id, lingua):
    l = getLanguage(chat_id)
    if 'português(br)' in lingua:
        bds.setLanguage(chat_id, 'ptBR')
        bds.setWaiting(chat_id, False)
        l = getLanguage(chat_id)
        return voltarMain(chat_id, l.mudar_lingua)
    elif 'english(us)' in lingua:
        bds.setLanguage(chat_id, 'enUS')
        bds.setWaiting(chat_id, False)
        l = getLanguage(chat_id)
        return voltarMain(chat_id, l.mudar_lingua)
    else:
        bds.setWaiting(chat_id, False)
        return voltarMain(chat_id, l.voltar_msg)
