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

def getKb(chat_id, kb, adm = None):
    l = getLanguage(chat_id)
    if kb == 'main':
        if bds.getEnabled(chat_id):
            if bds.getInGame(chat_id):
                return [ #getLetras
                    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
                    [l.comandos]
                ]
            if bds.getPreGame(chat_id):
                if adm:
                    print 'tem uid'
                    return [[l.entrar, l.sair], [l.cancelar_jogo, l.fechar_jogo], [l.comandos]]
                print 'nao'
                return [[l.entrar, l.sair], [l.comandos]]
            return [[l.novojogo], [l.ajuda, l.rank], [l.config], [l.desligar]] #possíveis keyboards
        return [[l.ligar]]
    elif kb == 'sec':
        if bds.getEnabled(chat_id):
            if bds.getInGame(chat_id):
                l.cancelar_jogo = l.cancelar_jogo if bds.checkAdm(chat_id, u_id) else None
                return [[l.cancelar_jogo], [l.ajuda, l.rank], [l.config], [l.voltar], [l.desligar]]
            if bds.getPreGame(chat_id):
                return [[l.ajuda, l.rank], [l.config, l.voltar], [l.desligar]]
            return [['Português(BR)', 'English(US)'], [l.ajuda], [l.voltar]] #possíveis keyboards
        return [[l.ligar]]


#Funções dos comandos
def start(chat_id, message_id):
    l = getLanguage(chat_id)
    if bds.getEnabled(chat_id):
        return toDict(chat_id, l.is_enabled)
    bds.setEnabled(chat_id, True)
    bds.checkChat(chat_id)
    l = getLanguage(chat_id)
    keyboard = makeKb(getKb(chat_id, 'main'), one_time_keyboard = True)
    return toDict(chat_id, l.start_msg, replyMarkup = keyboard)

def stop(chat_id):
    l = getLanguage(chat_id)
    bds.setEnabled(chat_id, False)
    keyboard = makeKb(getKb(chat_id, 'main'), resize_keyboard = True, one_time_keyboard = True)
    return toDict(chat_id, l.stop_msg, replyMarkup = keyboard)

def ajuda(chat_id):
    l = getLanguage(chat_id)
    if bds.getEnabled(chat_id):
        if bds.getSettings(chat_id).waiting:
            return toDict(chat_id, l.config_help_msg)
        if bds.getInGame(chat_id):
            return toDict(chat_id, l.in_game_help_msg)
        if bds.getPreGame(chat_id):
            return toDict(chat_id, l.pre_game_help_msg)
        return toDict(chat_id, l.start_help_msg)

def rank(chat_id):
    l = getLanguage(chat_id)
    return toDict(chat_id, 'Sem rank')

def novojogo(chat_id, u_id, u_name, message_id):
    l = getLanguage(chat_id)
    if (not bds.getPreGame(chat_id)):
        print 'primeiro'
        bds.setPreGame(chat_id, True, u_id = u_id, u_name = u_name, message_id = message_id)
        keyboard = makeKb(getKb(chat_id, 'main', adm = False), resize_keyboard = True, one_time_keyboard = True)
        return toDict(chat_id, l.inicial_msg, replyMarkup = keyboard)
    print 'segundo'
    keyboard = makeKb(getKb(chat_id, 'main', adm = True), resize_keyboard = True, one_time_keyboard = True, selective = True)
    return toDict(chat_id, l.inicialMsg(u_name), replyTo = message_id, replyMarkup = keyboard)

def voltar(chat_id, msg, tipo, u_id = None, message_id = None):
    adm = None
    if u_id:
        adm = bds.checkAdm(chat_id, u_id)
    if message_id:
        keyboard = makeKb(getKb(chat_id, tipo, adm = adm), resize_keyboard = True, selective = True, one_time_keyboard = True)
        return toDict(chat_id, msg, replyTo = message_id, replyMarkup = keyboard )
    keyboard = makeKb(getKb(chat_id, tipo, adm = adm), resize_keyboard = True, one_time_keyboard = True)
    return toDict(chat_id, msg, replyMarkup = keyboard )

def config(chat_id, message_id):
    l = getLanguage(chat_id)
    language_kb = [['Português(BR)', 'English(US)'], [l.ajuda], [l.voltar]]
    bds.setWaiting(chat_id, True)
    keyboard = makeKb(language_kb, resize_keyboard = True, selective = True, one_time_keyboard = True)
    return toDict(chat_id, l.linguas, replyTo = message_id, replyMarkup = keyboard)

def changeLanguage(chat_id, lingua, u_id):
    l = getLanguage(chat_id)
    if 'português(br)' in lingua:
        bds.setLanguage(chat_id, 'ptBR')
        bds.setWaiting(chat_id, False)
        l = getLanguage(chat_id)
        return voltar(chat_id, l.mudar_lingua, 'main', u_id = u_id)
    elif 'english(us)' in lingua:
        bds.setLanguage(chat_id, 'enUS')
        bds.setWaiting(chat_id, False)
        l = getLanguage(chat_id)
        return voltar(chat_id, l.mudar_lingua, 'main', u_id = u_id)
    elif l.voltar.lower() in lingua:
        bds.setWaiting(chat_id, False)
        return voltar(chat_id, l.voltar_msg, 'main', u_id = u_id)
    else:
        return toDict(chat_id, l.ocupado_msg)
