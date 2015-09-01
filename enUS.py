#-*- coding: utf-8 -*-
#Linguagem Inglês, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#Botões dos Keyboards
novojogo = 'New Game'
ajuda = 'Help'
rank = 'Rank'
ligar = 'Start'
desligar = 'Stop'
config = 'Settings'
voltar = 'Back'
cancelar = 'Cancel'

#Respostas iniciais
linguas = 'Choose your language:'
mudar_lingua = 'Change successfull'
start_msg = 'Hi, I am Forca Bot (HangMan) and I will help you to play hangman games!\nPress "new game" to start.'
is_enabled = 'Forca Bot is already on'
stop_msg = 'Forca Bot stopped'
start_help_msg = 'There is no game, please use "new game" to start one'
voltar_msg = 'Main menu'

#respostas PreGame
def inicialMsg(u_name):
    return 'Starting a new game!\n'+u_name+' will be the manager of this game!\nLets start defining the players of this game, who wants to join please choose Enter '+emoji_sorriso

#repostas InGame
