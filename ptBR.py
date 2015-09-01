#-*- coding: utf-8 -*-
#Linguagem Português, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#Botões dos Keyboards
novojogo = 'Novo Jogo'
ajuda = 'Ajuda'
rank = 'Rank'
ligar = 'Ligar'
desligar = 'Desligar'
config = 'Configurações'
voltar = 'Voltar'
cancelar = 'Cancelar'

#Respostas iniciais
linguas = 'Escolha sua linguagem:'
mudar_lingua = 'Mudança feita com sucesso'
start_msg = 'Olá, eu sou o Forca Bot e fui criado para organizar jogos da forca!\nAperte no botão "novo jogo" para começar!'
is_enabled = 'Forca Bot já está ligado'
stop_msg = 'Forca Bot desligado'
start_help_msg = 'Não há jogo em andamento, clique no botão "novo jogo" para começar um jogo'
voltar_msg = 'Menu inicial'

#respostas PreGame
def inicialMsg(u_name):
    return 'Começando um novo jogo!\n'+u_name+' será o administrador dessa rodada.\nVamos começar definindo os jogadores desta rodada, quem quiser participar escolha Entrar'+emoji_sorriso

#repostas InGame
