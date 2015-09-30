#-*- coding: utf-8 -*-
#Lógica do game

import comandos as c
import bds

def cancelarJogo(chat_id, u_id):
    l = c.getLanguage(chat_id)
    if bds.checkAdm(chat_id, u_id):
        bds.delGame(chat_id)
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True)
        return [c.toDict(chat_id, l.cancelar_jogo_msg, replyMarkup = keyboard)]
    return [c.toDict(chat_id, l.cantdo_msg)]

def chutarLetra(chat_id, u_id, message_id, letra):
    l = c.getLanguage(chat_id)
    r = bds.checkLetra(chat_id, u_id, letra)
    rpl = []
    if r == True: #Se acertou a letra
        rpl.append(c.toDict(chat_id, l.acertou_letra_msg, replyTo = message_id, replyMarkup = c.makeKbh(True, selective = True)))
        rpl.append(nextRound(chat_id))
    elif r == 2: #Se a letra já foi chutada
        rpl.append(c.toDict(chat_id, l.jachutada_msg))
    else: #Se errou a letra
        rpl.append(c.toDict(chat_id, l.errou_letra_msg, replyTo = message_id, replyMarkup = c.makeKbh(True, selective = True)))
        vida = bds.menosVida(chat_id)
        if vida == True: #Se acabou as vidas
            keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True)
            rpl.append(c.toDict(chat_id, l.gameover_msg, replyMarkup = keyboard))
        elif vida == 2: #Se resta somente uma vida
            rpl.append(c.toDict(chat_id, l.umavida_msg))
            rpl.append(nextRound(chat_id))
        else:
            rpl.append(nextRound(chat_id))
    return rpl

def nextRound(chat_id):
    l = c.getLanguage(chat_id)
    bds.roundPlus(chat_id)
    players = bds.getPlayers(chat_id)
    aRound = bds.getRound(chat_id)
    vidas = str(bds.getVidas(chat_id))
    keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, selective = True)
    return c.toDict(chat_id, (bds.getMascara(chat_id)+'\n'+l.vidas_msg+vidas+'\n'+l.nextPlayer(players[1][aRound]), replyTo = players[2][aRound], replyMarkup = keyboard)

def arriscarPalavra1(chat_id, u_id, message_id):
    l = c.getLanguage(chat_id)
    bds.setArriscarBlock(chat_id, True)
    return [c.toDict(chat_id, l.arriscar_msg, replyTo = message_id, replyMarkup = c.makeFr(True, selective = True))]

def arriscarPalavra2(chat_id, u_id, message_id, text):
    l = c.getLanguage(chat_id)
    bds.setArriscarBlock(chat_id, False)
    if bds.checkPalavra(chat_id, text):
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True)
        return [c.toDict(chat_id, l.venceu(u_name), replyMarkup = keyboard)]
    else:
        rm = bds.rmPlayer(chat_id, u_id, message_id)
        if rm == True:
            rpl = []
            rpl.append(c.toDict(chat_id, l.perdeu(u_name), replyTo = message_id, replyMarkup = c.makeKbh(True, selective = True)))
            rpl.append(nextRound(chat_id))
            return rpl
        elif rm == 'setAdm':
            rpl = []
            adm = bds.getAdm(chat_id)
            rpl.append(c.toDict(chat_id, l.perdeu(u_name), replyTo = message_id, replyMarkup = c.makeKbh(True, selective = True)))
            rpl.append(c.toDict(chat_id, l.novoAdmMsg(adm[1])))
            rpl.append(nextRound(chat_id))
            return rpl
        else:
            keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True)
            return [c.toDict(chat_id, l.perdeu_msg, replyMarkup = keyboard)]
