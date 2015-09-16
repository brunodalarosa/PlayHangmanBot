#-*- coding: utf-8 -*-
#Lógica do game

import comandos as c
import bds

def cancelarJogo(chat_id, u_id):
    l = c.getLanguage(chat_id)
    if bds.checkAdm(chat_id, u_id):
        bds.delGame(chat_id)
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
        return [c.toDict(chat_id, l.cancelar_jogo_msg, replyMarkup = keyboard)]
    return [c.toDict(chat_id, l.cantdo_msg)]

def arriscarPalavra1(chat_id, u_id):
    l = c.getLanguage(chat_id)
    if bds.checkRound(chat_id, u_id):
        bds.setArriscarBlock(chat_id, True)
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
        return [c.toDict(chat_id, l.arriscar_msg, replyMarkup = keyboard)]
    else:
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
        return [c.toDict(chat_id, l.round_errado_msg, replyMarkup = keyboard)]

def arriscarPalavra2(chat_id, u_id, text):
    l = c.getLanguage(chat_id)
    if bds.checkRound(chat_id, u_id):
        if bds.checkPalavra(chat_id,text):
            bds.delGame(chat_id)
            bds.setArriscarBlock(chat_id, False)
            keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
            return [c.toDict(chat_id, l.venceu_msg, replyMarkup = keyboard)]
        else:
            bds.delGame(chat_id)
            bds.setArriscarBlock(chat_id, False)
            keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
            return [c.toDict(chat_id, l.perdeu_msg, replyMarkup = keyboard)]
    else:
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
        return [c.toDict(chat_id, l.round_errado_msg, replyMarkup = keyboard)]
