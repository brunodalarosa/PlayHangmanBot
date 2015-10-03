#-*- coding: utf-8 -*-
#Contém a lógica do preGame

#Importa os comandos
import comandos as c
import bds
import game as g
from random import randint, shuffle

def entrar(chat_id, u_id, u_name, message_id):
    l = c.getLanguage(chat_id)
    if bds.addPlayer(chat_id, u_id, u_name, message_id):
        kb = c.makeKb(c.getKb(chat_id,'main',u_id = u_id)[0], selective = True, resize_keyboard = True)
        return [c.toDict(chat_id, l.entrarMsg(u_name), replyTo = message_id, replyMarkup = kb )]
    return [c.toDict(chat_id, l.esta_dentro_msg)]

def sair(chat_id, u_id, u_name, message_id):
    aux = bds.rmPlayer(chat_id, u_id, message_id)
    l = c.getLanguage(chat_id)
    if aux == False:
        kb = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True)
        return [c.toDict(chat_id, l.sem_jogador_msg, replyMarkup = kb)]
    elif aux == 'setAdm':
        rpl = []
        pl = bds.getPlayers(chat_id)
        kb = c.makeKb(c.getKb(chat_id, 'main', u_id = u_id)[0], selective = True, resize_keyboard = True)
        rpl.append(c.toDict(chat_id, l.playerQuitMsg(u_name), replyTo = message_id, replyMarkup = kb))
        kb = c.makeKb(c.getKb(chat_id,'main')[1], resize_keyboard = True, selective = True)
        rpl.append(c.toDict(chat_id, l.novoAdmMsg(pl[1][0]), replyTo = pl[2][0], replyMarkup = kb))
        return rpl
    elif aux == True:
        kb = c.makeKb(c.getKb(chat_id,'main',u_id = u_id)[0], selective = True, resize_keyboard = True)
        return [c.toDict(chat_id, l.playerQuitMsg(u_name), replyTo = message_id, replyMarkup = kb)]
    elif aux == 'semPlayer':
        return [c.toDict(chat_id, l.is_out_msg)]

def fecharJogo(chat_id, u_id, message_id, date):
    l = c.getLanguage(chat_id)
    rpl = []
    if bds.checkAdm(chat_id, u_id):
        bds.setPreGame(chat_id, False)
        bds.setInGame(chat_id, True)
        categoria = randint(0, (len(l.palavras)-1))
        palavra = randint(1, (len(l.palavras[categoria])-1))
        palavra = l.palavras[categoria][palavra]
        categoria = l.palavras[categoria][0]
        mascara = bds.setCP(chat_id, categoria, palavra)
        vidas = bds.setVidas(chat_id)
        bds.shufflePlayers(chat_id, date)
        u_names = bds.getPlayers(chat_id)[1]
        message_ids = bds.getPlayers(chat_id)[2]
        ordem = ''
        for i in range(len(u_names)):
            ordem = ordem+u_names[i]+'\n'
        kb = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True, selective = True)
        rpl.append(c.toDict(chat_id, l.close_game_msg, replyMarkup = c.makeKbh(True)))
        rpl.append(c.toDict(chat_id, ordem, replyTo = message_ids[0], replyMarkup = kb))
        rpl.append(c.toDict(chat_id, l.categoria_msg+categoria))
        rpl.append(c.toDict(chat_id, l.palavra_msg+mascara))
        rpl.append(c.toDict(chat_id, l.vidas_msg+g.vidasEmoji(chat_id)))
        return rpl
    return [c.toDict(chat_id, l.cantdo_msg)]

def cancelarJogo(chat_id, u_id):
    l = c.getLanguage(chat_id)
    if bds.checkAdm(chat_id, u_id):
        bds.delGame(chat_id)
        keyboard = c.makeKb(c.getKb(chat_id, 'main')[0], resize_keyboard = True)
        return [c.toDict(chat_id, l.cancelar_jogo_msg, replyMarkup = keyboard)]
    return [c.toDict(chat_id, l.cantdo_msg)]
