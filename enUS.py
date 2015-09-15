#-*- coding: utf-8 -*-
#Linguagem Inglês, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Category1', 'word1', 'word2'],
                ['Category2', 'wor1', 'wor2']
            ]

#Botões dos Keyboards
novojogo = 'New Game'
ajuda = 'Help'
rank = 'Rank'
ligar = 'Start'
desligar = 'Stop'
config = 'Settings'
voltar = 'Back'
cancelar = 'Cancel'
comandos = 'Commands'
entrar = 'Join'
sair = 'Quit'
fechar_jogo = 'Close game'
cancelar_jogo = 'Cancel game'

#Respostas iniciais
linguas = 'Choose your language:'
iniciar_msg = 'Starting'
mudar_lingua = 'Change successfull'
start_msg = 'Hi, I am Forca Bot (HangMan) and I will help you to play hangman games!\nPress "new game" to start.'
is_enabled = 'Forca Bot is already on'
stop_msg = 'Forca Bot stopped'
start_help_msg = 'There is no game, please use "new game" to start one'
config_help_msg = 'Choose the language of the Bot\nPs.: The words for the game depends on the language'
pre_game_help_msg = 'The game is open to people to join\nManager: use Close Game to close the game and start or Cancel Game to cancel it'
in_game_help_msg = 'Clique nas letras para chuta-las, se quiser mais opções vá em Comandos'
voltar_msg = 'Main menu'
comandos_msg = 'Commands'
ocupado_msg = 'Bot occupied'
esta_dentro_msg = 'You are already in this game'
cancelar_jogo_msg = 'Game canceled by the manager'

#respostas PreGame
def inicialMsg(u_name):
    return 'Starting a new game!\n'+u_name+' will be the manager of this game!'
inicial_msg = 'Lets start defining the players of this game, who wants to join please choose Enter '+emoji_sorriso

def entrarMsg(u_name):
    return 'Ok '+u_name+', você vai participar dessa rodada\nSe quiser sair é só usar o Sair'

#repostas InGame
