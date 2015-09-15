#-*- coding: utf-8 -*-
#Contém a lógica do preGame

#Importa os comandos
import comandos as c
import bds

def entrar(chat_id, u_id, u_name, message_id):
    l = c.getLanguage(chat_id)
    if bds.addPlayer(chat_id, u_id, u_name, message_id):
        return [c.toDict(chat_id, l.entrarMsg(u_name))]
    return [c.toDict(chat_id, l.esta_dentro_msg)]

def sair(chat_id, u_id, u_name, message_id):
    aux = bds.rmPlayer(chat_id, u_id, message_id)
    l = c.getLanguage(chat_id)
    if aux == False:
        kb = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
        return [c.toDict(chat_id, l.sem_jogador_msg, replyMarkup = kb)]
    elif aux == 'setAdm':
        rpl = []
        pl = bds.getPlayers(chat_id)
        kb = c.makeKb(c.getKb(chat_id,'main')[0], resize_keyboard = True, one_time_keyboard = True, selective = True)
        rpl.append(c.toDict(chat_id, l.playerQuitMsg(u_name), replyTo = message_id, replyMarkup = kb))
        kb = c.makeKb(c.getKb(chat_id,'main')[1], resize_keyboard = True, one_time_keyboard = True, selective = True)
        rpl.append(c.toDict(chat_id, l.novoAdmMsg(pl[1][0]), replyTo = pl[2][0], replyMarkup = kb))
        return rpl
    elif aux == True:
        return [c.toDict(chat_id, l.playerQuitMsg(u_name))]
    elif aux == 'semPlayer':
        return [c.toDict(chat_id, l.is_out_msg)]

def fecharJogo(chat_id, u_id):
    l = c.getLanguage(chat_id)
    return [c.toDict(chat_id, 'sem jogo ainda')]

def cancelarJogo(chat_id, u_id):
    l = c.getLanguage(chat_id)
    if bds.checkAdm(chat_id, u_id):
        bds.delGame(chat_id)
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
        return [c.toDict(chat_id, l.cancelar_jogo_msg, replyMarkup = keyboard)]
