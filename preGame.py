#-*- coding: utf-8 -*-
#Contém a lógica co preGame

#Importa os comandos
import comandos as c
import bds

def entrar(chat_id, u_id, u_name, message_id):
    l = c.getLanguage(chat_id)
    if bds.addPlayer(chat_id, u_id, u_name, message_id):
        return c.toDict(chat_id, l.entrarMsg(u_name))
    return c.toDict(chat_id, l.esta_dentro_msg)

def fecharJogo(chat_id, u_id):
    return toDict(chat_id, 'sem jogo ainda')

def cancelarJogo(chat_id, u_id):
    print 'cancelar'
    l = c.getLanguage(chat_id)
    if bds.checkAdm(chat_id, u_id):
        bds.delGame(chat_id)
        keyboard = c.makeKb(c.getKb(chat_id, 'main'), resize_keyboard = True, one_time_keyboard = True)
        return c.toDict(chat_id, l.cancelar_jogo_msg, replyMarkup = keyboard)
