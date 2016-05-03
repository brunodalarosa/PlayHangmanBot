#-*- coding: utf-8 -*-
#Arquivo com as funções dos comandos executados (melhorar)

#TODO
#Arrumar casos do kb

#Standard imports
import json
import bds
from emojis import *

#Lê as configurações
def getLanguage(chat_id):
    s = bds.getSettings(chat_id) #Classe settings
    if s.language == 'ptBR':
        import ptBR as l
        return l
    elif s.language == 'enUS':
        import enUS as l
        return l
    elif s.language == 'hbIL':
        import hbIL as l
        return l
    return

#Recebe os dados que serão repondidos e transforma em um dict
def toDict(chat_id, text, replyTo = None, replyMarkup = None):
    #chat_id = int(chat_id)
    if replyMarkup:
        if replyTo:
            d = dict(chat_id = chat_id, text = text, reply_to_message_id = replyTo, reply_markup = replyMarkup)
            return d
        d = dict(chat_id = chat_id, text = text, reply_markup = replyMarkup)
        return d
    d = dict(chat_id = chat_id, text = text)
    return d

def makeFr(force_reply, selective = None):
    selective = selective if selective else False
    return json.dumps({'force_reply':force_reply, 'selective':selective})

def makeKbh(hide_keyboard, selective = None):
    selective = selective if selective else False
    return json.dumps({'hide_keyboard':hide_keyboard, 'selective':selective})

#Recebe uma matriz e a transforma em um teclado personalizado
def makeKb(kb, resize_keyboard = None, one_time_keyboard = None, selective = None):
    resize_keyboard = resize_keyboard if resize_keyboard else False
    one_time_keyboard = one_time_keyboard if one_time_keyboard else False
    selective = selective if selective else False
    return json.dumps({'keyboard':kb, 'resize_keyboard':resize_keyboard, 'one_time_keyboard':one_time_keyboard, 'selective':selective})

def getKb(chat_id, k, u_id = None):
    l = getLanguage(chat_id)
    kb = []
    if k == 'main':
        if bds.getEnabled(chat_id):
            if bds.getInGame(chat_id):
                if bds.getArriscarBlock(chat_id):
                    kb.append([[l.voltar]])
                else:
                    letras = bds.getLetras(chat_id)
                    kb.append([letras[0], letras[1], letras[2], [l.arriscar], [l.comandos]]) #letters keyboard
            elif bds.getPreGame(chat_id):
                if u_id in bds.getPlayers(chat_id)[0]:
                    kb.append([[l.sair], [l.comandos]]) #Pre-game in
                else:
                    kb.append([[l.entrar], [l.comandos]]) #Pre-game out
                kb.append([[l.cancelar_jogo, l.fechar_jogo],[l.categorias_btn], [l.comandos]]) #Pre-game admin
            else:
                kb.append([[l.novojogo], [l.ajuda, l.rank], [l.config, l.sobre], [l.desligar]]) #Main
        else:
            kb.append([[l.ligar]]) #Off
    elif k == 'cmd':
        if bds.getInGame(chat_id):
            kb.append([[l.ajuda, l.rank], [l.config], [l.voltar], [l.desligar]])
            kb.append([[l.cancelar_jogo], [l.ajuda, l.rank], [l.config, l.voltar], [l.desligar]])
        elif bds.getPreGame(chat_id):
            kb.append([[l.ajuda, l.rank], [l.config, l.voltar], [l.desligar]])
    elif k == 'config':
        kb.append([['Português(BR)' + emoji_br, 'English(US)' + emoji_usa, 'עברית (ישראל)' + emoji_hb], [l.ajuda], [l.voltar]])
    elif k == 'fora':
        kb.append([[l.esta_fora]])
    elif k == 'first':
        kb.append([['Português(BR)' + emoji_br, 'English(US)' + emoji_usa, 'עברית (ישראל)' + emoji_hb]])
    if (len(kb) == 0):
        kb = [[l.att_kb]]
    return kb


#Funções dos comandos
def start(chat_id, u_id, first):
    if not first:
        l = getLanguage(chat_id)

        rpl = []
        if bds.getEnabled(chat_id):
            return [toDict(chat_id, l.is_enabled)]
        bds.setEnabled(chat_id, True)
        bds.checkChat(chat_id)
        l = getLanguage(chat_id)
        kb = getKb(chat_id, 'main', u_id = u_id)
        if (len(kb) != 1):
            adm = bds.getAdm(chat_id)
            keyboard = makeKb(kb[0], resize_keyboard = True)
            rpl.append(toDict(chat_id, l.iniciar_msg, replyMarkup = keyboard))
            keyboard = makeKb(kb[1], resize_keyboard = True, selective = True)
            rpl.append(toDict(chat_id, l.start_msg, replyTo = adm[2], replyMarkup = keyboard))
        else:
            keyboard = makeKb(kb[0], resize_keyboard = True)
            rpl.append(toDict(chat_id, l.start_msg, replyMarkup = keyboard))
        return rpl
    bds.setFirst(chat_id)
    bds.setEnabled(chat_id,True)
    kb = makeKb(getKb(chat_id, 'first')[0], resize_keyboard = True)
    rpl = []
    rpl.append(toDict(chat_id, 'Im the PlayHangmanBot, please choose a language:', replyMarkup = kb))
    rpl.append(toDict('-27626712', 'Novo chat criado: '+chat_id))
    return rpl

def stop(chat_id):
    l = getLanguage(chat_id)
    bds.setEnabled(chat_id, False)
    keyboard = makeKb(getKb(chat_id, 'main')[0], resize_keyboard = True)
    return [toDict(chat_id, l.stop_msg, replyMarkup = keyboard)]

def sobre(chat_id):
    l = getLanguage(chat_id)
    return [toDict(chat_id, l.about_msg)]

def ajuda(chat_id):
    l = getLanguage(chat_id)
    if bds.getEnabled(chat_id):
        if bds.getSettings(chat_id).waiting:
            return [toDict(chat_id, l.config_help_msg)]
        if bds.getInGame(chat_id):
            return [toDict(chat_id, l.in_game_help_msg)]
        if bds.getPreGame(chat_id):
            return [toDict(chat_id, l.pre_game_help_msg)]
        return [toDict(chat_id, l.start_help_msg)]

def rank(chat_id):
    l = getLanguage(chat_id)
    rank = bds.getRank(chat_id)
    ranking = l.ranking_msg+'\n'
    if len(rank) > 0:
        for i in range(len(rank[0])):
            ranking = ranking+rank[0][i]+' - '+str(rank[1][i])+'\n'
    return [toDict(chat_id, ranking)]

def kb(chat_id, u_id, message_id, waiting):
    l = getLanguage(chat_id)
    kb = getKb(chat_id, 'main', u_id = u_id)
    keyboard = makeKb(kb[0], resize_keyboard = True, selective = True)
    if bds.getEnabled(chat_id):
        if (bds.getInGame(chat_id)) or (not bds.getPreGame(chat_id)):
            i = 0
        elif bds.getPreGame(chat_id):
            i = 0
            if bds.checkAdm(chat_id, u_id):
                i = 1
    else:
        i = 0
    keyboard = makeKb(kb[i], resize_keyboard = True, selective = True)
    if waiting:
        kb = getKb(chat_id, 'config')
        keyboard = makeKb(kb[0], resize_keyboard = True, selective = True)
    return [toDict(chat_id, l.teclado_msg, replyTo = message_id, replyMarkup = keyboard)]


def novojogo(chat_id, u_id, u_name, message_id):
    l = getLanguage(chat_id)
    rpl = []
    bds.setPreGame(chat_id, True, u_id = u_id, u_name = u_name, message_id = message_id)
    kb = getKb(chat_id, 'main')
    keyboard = makeKb(kb[0], resize_keyboard = True)
    rpl.append(toDict(chat_id, l.inicial_msg, replyMarkup = keyboard))
    keyboard = makeKb(kb[1], resize_keyboard = True, selective = True)
    rpl.append(toDict(chat_id, l.inicialMsg(u_name), replyTo = message_id, replyMarkup = keyboard))
    return rpl

def voltar(chat_id, msg, message_id, u_id, esp = None):
    rpl = []
    i = 0
    if bds.getSettings(chat_id).waiting:
        bds.setWaiting(chat_id, False)
        if bds.getInGame(chat_id):
            kb = getKb(chat_id, 'cmd')
            if not bds.checkAdm(chat_id, u_id):
                i = 0
            else:
                i = 1
        elif bds.getPreGame(chat_id):
            kb = getKb(chat_id, 'cmd')
            i = 0
        else:
            kb = getKb(chat_id, 'main')
            i = 0
    else:
        if bds.getArriscarBlock(chat_id):
            bds.setArriscarBlock(chat_id, False)
        kb = getKb(chat_id, 'main', u_id = u_id)
        if len(kb) != 1:
            if not bds.checkAdm(chat_id, u_id):
                i = 0
            else:
                i = 1
    if not esp:
        keyboard = makeKb(kb[i], resize_keyboard = True, selective = True)
        rpl.append(toDict(chat_id, msg, replyTo = message_id, replyMarkup = keyboard))
    else:
        keyboard = makeKb(kb[0], resize_keyboard = True)
        rpl.append(toDict(chat_id, msg, replyMarkup = keyboard))
        if len(kb) != 1:
            keyboard = makeKb(kb[1], resize_keyboard = True, selective = True)
            rpl.append(toDict(chat_id, msg, replyTo = message_id, replyMarkup = keyboard))
    return rpl

def config(chat_id, message_id):
    l = getLanguage(chat_id)
    bds.setWaiting(chat_id, True)
    keyboard = makeKb(getKb(chat_id, 'config')[0], resize_keyboard = True, selective = True)
    return [toDict(chat_id, l.linguas, replyTo = message_id, replyMarkup = keyboard)]

def comandos(chat_id, message_id, u_id):
    l = getLanguage(chat_id)
    kb = getKb(chat_id, 'cmd')
    if not (bds.getInGame(chat_id) and bds.checkAdm(chat_id, u_id)):
        keyboard = makeKb(kb[0], resize_keyboard = True, selective = True)
    else:
        keyboard = makeKb(kb[1], resize_keyboard = True, selective = True)
    return [toDict(chat_id, l.comandos_msg, replyTo = message_id, replyMarkup = keyboard)]

def changeLanguage(chat_id, lingua, message_id, u_id):
    l = getLanguage(chat_id)
    if 'português(br)' in lingua:
        bds.setLanguage(chat_id, 'ptBR')
        l = getLanguage(chat_id)
        if bds.getFirstWelcome(chat_id)[1]:
            bds.setWelcome(chat_id)
            return voltar(chat_id, l.start_msg, message_id, u_id, esp = True)
        return voltar(chat_id, l.mudar_lingua, message_id, u_id, esp = True)
    elif 'english(us)' in lingua:
        bds.setLanguage(chat_id, 'enUS')
        l = getLanguage(chat_id)
        if bds.getFirstWelcome(chat_id)[1]:
            bds.setWelcome(chat_id)
            return voltar(chat_id, l.start_msg, message_id, u_id, esp = True)
        return voltar(chat_id, l.mudar_lingua, message_id, u_id, esp = True)
    elif 'עברית (ישראל)' in lingua:
        bds.setLanguage(chat_id, 'hbIL')
        l = getLanguage(chat_id)
        if bds.getFirstWelcome(chat_id)[1]:
            bds.setWelcome(chat_id)
            return voltar(chat_id, l.start_msg, message_id, u_id, esp = True)
        return voltar(chat_id, l.mudar_lingua, message_id, u_id, esp = True)
    elif l.voltar.lower() in lingua:
        return voltar(chat_id, l.voltar_msg, message_id, u_id)
    else:
        return [toDict(chat_id, l.ocupado_msg)]
