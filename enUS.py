#-*- coding: utf-8 -*-
#Linguagem Inglês, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Things', 'Chair', 'Fire', 'Oven', 'Strings'],
                ['Games', 'League of Legends', 'Defence of the Ancient', 'Tree of savior', 'Spore']
            ]

#Botões dos Keyboards
novojogo = 'New Game' + emoji_joystick
ajuda = 'Help' + emoji_light
rank = 'Rank' + emoji_trofeu
ligar = 'Start' + emoji_foguete
desligar = 'Stop' + emoji_x
config = 'Settings' + emoji_ferramenta
voltar = 'Back' + emoji_back
cancelar = 'Cancel' + emoji_x
comandos = 'Commands' + emoji_light
entrar = 'Join' + emoji_foguete
sair = 'Quit' + emoji_x
fechar_jogo = 'Start Game' + emoji_foguete
cancelar_jogo = 'Cancel game' + emoji_x
arriscar = 'Risk!' + emoji_gritar
esta_fora = 'You are out of this game' + emoji_proibido

#Respostas iniciais
linguas = emoji_planeta + 'Choose a language:'
iniciar_msg = 'Loading...'
mudar_lingua = 'Change successful' + emoji_thumbsUp
start_msg = 'Hi, i am the Forca bot, the master of Hangman games! My duty is to organize and play Hangman games with you and your friends and ensure that we will have fun!\n Press the "new game" button and we shall begin!' + emoji_sorriso
is_enabled = 'Im already ready!'
stop_msg = 'Turning off'
start_help_msg = 'There is no game happening right now, press the button "new game" to start one or press "Rank" to see the ranking.\n You can also change the settings if you want to' + emoji_sorriso
config_help_msg = 'Choose the language you want.\nObs.: The secrets words of the games depends on the selected language'
voltar_msg = 'Main menu'
cantdo_msg = 'You cant do this'
comandos_msg = 'Commands'
ocupado_msg = 'I am busy right now, sorry' + emoji_triste
teclado_msg = 'Keyboard'
ranking_msg = emoji_coroa + ' RANKING ' + emoji_coroa

#respostas PreGame
def inicialMsg(u_name):
    return 'Starting a new game! \n'+u_name+' will the admin of this game.' + emoji_oculos

inicial_msg = 'Lets begin defining the players, who wants to enter press the "Enter" button!'+emoji_sorriso
close_game_msg = 'The game will begin! In your turn press a letter to guess it or press "Risk" if you think that already discovered the secret word, but be careful, there is no way back!'+emoji_zoando+'\n We will play in this order:'
palavra_msg = 'The secret word: '
categoria_msg = 'Category: '
esta_dentro_msg = 'You already in this game!'
sem_jogador_msg = 'All the players quited, the game will be canceled! ' + emoji_surpreso
cancelar_jogo_msg = 'Game canceled by the admin'
is_out_msg = 'You are not in this game' + emoji_lua
vidas_msg = 'Lifes: '
pre_game_help_msg = 'I am waiting for people to join the game, press "Enter" to join \nAdmin: Press "Start game" to begin the game with this players'

def novoAdmMsg(u_name):
    return 'A new admin was selected! '+u_name+' is the new admin.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'The player '+u_name+' quited.' + emoji_triste

def entrarMsg(u_name):
    return 'Ok '+u_name+', you will play in this game' + emoji_blink

#repostas InGame
in_game_help_msg = 'Press the letter to guess them or press "Risk" if you think that already know the secret word! If you want to see more options press the "Commands" button'
arriscar_msg = 'So you think that you know what is the secret word? ' + emoji_zoando + ' Send me the word, but think wisely, if you fail you will be eliminated!' + emoji_lua
round_errado_msg = 'It is not your time to play yet! Wait for your turn!' + emoji_lua
acertou_letra_msg = 'Right letter!' + emoji_claps
errou_letra_msg = 'Wrong letter' + emoji_triste
jachutada_msg = 'This letter has already been guessed' + emoji_surpreso
umavida_msg = 'One life left! Discover the secret word or face your DEFEAT!' + emoji_lua
gameover_msg = emoji_poop + ' GAME OVER LOSERS! ' + emoji_poop
fora_msg = 'You are not in this game, wait for this game end to enter in another one!'

def perdeu(u_name):
    return u_name + ' Risked it all and losed! The player was eliminated!' + emoji_lua

def nextPlayer(u_name):
    return 'Turn of ' + u_name + ' ' + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Congratulations ' + u_name + ' you discovered the secret word and won the game! ' + emoji_confetti + '\n Score calculated and ranking updated! ' + emoji_sorriso
