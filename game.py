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

'''def chutar(chat_id, letra, u_id):
    l = c.getLanguage(chat_id)
    if bds.checkRound(chat_id, u_id):
        if bds.checkLetra(chat_id, letra):
            if letra in bds.getPalavra(chat_id):
                mascara = bds.getMascara(chat_id, letra)
            else:
                'errou'
        else:
             'essa letra foi chutada'
    else:
        'nao é sua vez'            '''

def arriscarPalavra1(chat_id, u_id, message_id):
    l = c.getLanguage(chat_id)
    if bds.checkRound(chat_id, u_id):
        bds.setArriscarBlock(chat_id, True)
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True, selective = True)
        return [c.toDict(chat_id, l.arriscar_msg, replyTo = message_id, replyMarkup = keyboard)]
    else:
        return [c.toDict(chat_id, l.round_errado_msg)]

def arriscarPalavra2(chat_id, u_id, message_id, text):
    l = c.getLanguage(chat_id)
    if bds.checkRound(chat_id, u_id):
        if bds.checkPalavra(chat_id,text):
            keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
            return [c.toDict(chat_id, l.venceu_msg, replyMarkup = keyboard)]
        else:
            rm = bds.rmPlayer(chat_id, u_id, message_id)
            keyboard = c.makeKb(c.getKb(chat_id, 'fora')[0], resize_keyboard = True, one_time_keyboard = True)
            if rm == True:
                return [c.toDict(chat_id, l.perdeu_msg, replyTo = message_id, replyMarkup = keyboard)]
            elif rm == 'setAdm':
                pl = bds.getPlayers(chat_id)
                rpl = []
                rpl.append(c.toDict(chat_id, l.perdeu_msg, replyTo = message_id, replyMarkup = keyboard))
                rpl.append(c.toDict(chat_id, l.novoAdmMsg(pl[1][0])))
                return rpl
            else:
                keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, one_time_keyboard = True)
                return [c.toDict(chat_id, l.perdeu_msg, replyMarkup = keyboard)]
    else:
        return [c.toDict(chat_id, l.round_errado_msg)]
